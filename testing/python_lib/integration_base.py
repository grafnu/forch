"""Integration test base class for Forch"""

import subprocess
import unittest
import os
import sys
import time
import yaml

import logging
logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class IntegrationTestBase(unittest.TestCase):
    """Base class for integration tests"""

    STACK_OPTIONS = {
        'setup_warmup_sec': 20,
        'skip-conn-check': True,
        'no-clean': True
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self._clean_stack()
        self._setup_stack()

    def tearDown(self):
        self._clean_stack()

    def _run_command(self, command, strict=True, capture=True):
        code, out, err = self._reap_process_command(self._run_process_command(command, capture))
        if strict and code:
            logger.warning('stdout: \n' + out)
            logger.warning('stderr: \n' + err)
            raise Exception('Command execution failed: %s' % str(command))
        return code, out, err

    def _run_process_command(self, command, capture):
        command_list = command.split() if isinstance(command, str) else command
        pipeout = subprocess.PIPE if capture else None
        return subprocess.Popen(command_list, stdout=pipeout, stderr=pipeout)

    def _reap_process_command(self, process):
        process.wait()
        stdout, stderr = process.communicate()
        strout = str(stdout, 'utf-8') if stdout else None
        strerr = str(stderr, 'utf-8') if stderr else None
        return process.returncode, strout, strerr

    def _run_cmd(self, cmd, arglist=[]):
        """Runs cmds from forch base folder"""
        path = os.path.dirname(os.path.abspath(__file__)) + '/../../'
        command = [path + cmd] + arglist
        code, _, _ = self._run_command(command, capture=False)
        print('return code %d: %s' % (code, cmd))
        assert code == 0, 'Execution failed: %s' % cmd

    def _setup_stack(self, options=STACK_OPTIONS):
        logger.debug("STACK_OPTIONS = %s", str(options))
        stack_args = []
        stack_args.extend(['local'] if options.get('local') else [])
        devices = options.get('devices')
        stack_args.extend(['devices', str(devices)] if devices else [])
        switches = options.get('switches')
        stack_args.extend(['switches', str(switches)] if devices else [])
        stack_args.extend(['skip-conn-check'] if options.get('skip-conn-check') else [])
        stack_args.extend(['dhcp'] if options.get('dhcp') else [])
        stack_args.extend(['no-clean'] if options.get('no-clean') else [])
        mode = options.get('mode')
        stack_args.extend([mode] if mode else [])

        logger.info('setup_stack ' + ' '.join(stack_args))
        self._run_cmd('bin/setup_stack', stack_args)
        time.sleep(options.get('setup_warmup_sec'))

    def _clean_stack(self):
        self._run_cmd('bin/net_clean')

    def _ping_host(self, container, host, count=1, output=False):
        return self._ping_host_reap(
            self._ping_host_process(container, host, count=count),
            output=output)

    def _ping_host_process(self, container, host, count=1):
        logger.debug('Trying to ping %s from %s' % (host, container))
        ping_cmd = 'docker exec %s ping -c %d %s' % (container, count, host)
        return self._run_process_command(ping_cmd, True)

    def _ping_host_reap(self, process, expected=False, output=False):
        print('phr1')
        return_code, out, err = self._reap_process_command(process)
        print('phr2')
        unexpected = not expected if return_code else expected
        print('phr3')
        if unexpected or output:
            print('phr4')
            logger.warning('ping with %s', str(process.args))
            logger.warning(out)
            print('phr5')
            print('Ping return code: %d' % return_code)
            print('phr6')
            print('stderr: %s' % err)
            print('phr8')
        print('phr7')
        return False if return_code else out.count('time=')

    def _fail_egress_link(self, alternate=False, restore=False):
        switch = 't1sw2' if alternate else 't1sw1'
        command = 'up' if restore else 'down'
        self._run_command('sudo ip link set %s-eth28 %s' % (switch, command),
                          capture=False)

    def _read_yaml_from_file(self, filename):
        with open(filename) as config_file:
            yaml_object = yaml.load(config_file, yaml.SafeLoader)
        return yaml_object

    def _read_faucet_config(self):
        filename = self._get_faucet_config_path()
        return self._read_yaml_from_file(filename)

    def _write_yaml_to_file(self, filename, yaml_object):
        with open(filename, 'w') as config_file:
            yaml.dump(yaml_object, config_file)

    def _write_faucet_config(self, config):
        filename = self._get_faucet_config_path()
        return self._write_yaml_to_file(filename, config)

    def _get_faucet_config_path(self):
        return os.path.dirname(os.path.abspath(__file__)) + \
            '/../../inst/forch-faucet-1/faucet/faucet.yaml'


if __name__ == '__main__':
    unittest.main()
