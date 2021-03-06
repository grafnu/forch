"""Integration test base class for Forch"""

import datetime
import re
import time
import unittest
from unittest.mock import create_autospec
import yaml

import dateutil.tz

from integration_base import IntegrationTestBase
from unit_base import FaucetizerTestBase, PortsStateManagerTestBase

from forch.port_state_manager import PortStateManager
from forch.utils import dict_proto

from forch.proto.devices_state_pb2 import DeviceBehavior, DevicePlacement, DevicesState
from forch.proto.forch_configuration_pb2 import OrchestrationConfig

class FotFaucetizerTestCase(FaucetizerTestBase):
    """Faucetizer test"""

    FORCH_CONFIG = """
    orchestration:
      unauthenticated_vlan: 100
      sequester_config:
        vlan_start: 1500
        vlan_end: 1699
        port_description: TESTING
    """

    def test_device_states(self):
        """test Faucet behavioral config generation at different devices states"""

        placements = [
            # mocking static placements
            ('02:0A:00:00:00:01', {'switch': 't2sw1', 'port': 1, 'connected': True}, True),
            # devices dynamically learned
            ('02:0b:00:00:00:02', {'switch': 't2sw2', 'port': 1, 'connected': True}, False),
        ]

        behaviors = [
            # mocking static behaviors
            ('02:0a:00:00:00:01', {'segment': 'SEG_A', 'role': 'red'}, True),
            # devices to be sequestered
            ('02:0a:00:00:00:01', {'segment': 'TESTING'}, False),
            ('02:0B:00:00:00:02', {'segment': 'TESTING'}, False),
            # devices to be operational
            ('02:0B:00:00:00:02', {'segment': 'SEG_B'}, False),
        ]

        # process static device info
        self._process_device_placement(placements[0])
        self._process_device_behavior(behaviors[0])

        # devices are learned and sent to sequestering
        self._process_device_placement(placements[1])
        self._process_device_behavior(behaviors[1])
        self._process_device_behavior(behaviors[2])

        expected_config = yaml.safe_load(self.FAUCET_BEHAVIORAL_CONFIG)
        self._update_port_config(
            expected_config, switch='t2sw1', port=1, native_vlan=200, role='red')
        self._update_port_config(expected_config, switch='t2sw2', port=1, native_vlan=1501)
        self._update_port_config(expected_config, switch='t1sw1', port=4, tagged_vlans=[272, 1501])

        # devices allowed to be operational
        self._process_device_behavior(behaviors[3])

        expected_config = yaml.safe_load(self.FAUCET_BEHAVIORAL_CONFIG)
        self._update_port_config(
            expected_config, switch='t2sw1', port=1, native_vlan=200, role='red')
        self._update_port_config(expected_config, switch='t2sw2', port=1, native_vlan=300)


def encapsulate_mac_port_behavior(mac, port_behavior):
    """Converts to proto object for mac port behavior"""
    devices_state_map = {
        'device_mac_behaviors': {
            mac: {'port_behavior': port_behavior}
        }
    }
    return dict_proto(devices_state_map, DevicesState)


class FotPortStatesTestCase(PortsStateManagerTestBase):
    """Test access port states"""

    def _process_device_placement(self, mac, device_placement, static=False):
        print(f'Received device placement for device {mac}: {device_placement}, {static}')
        self._received_device_placements.append((mac, device_placement.connected, static))
        if device_placement.connected:
            self._device_placements[mac] = device_placement
        else:
            self._device_placements.pop(mac)

    def _process_device_behavior(self, mac, device_behavior, static=False):
        print(f'Received device behavior for device {mac}: {device_behavior}, {static}')
        self._received_device_behaviors.append((mac, device_behavior.segment, static))

    def _get_vlan_from_segment(self, segment):
        segments_to_vlans = {
            'SEG_A': 100, 'SEG_B': 200, 'SEG_C': 300, 'SEG_D': 400, 'SEG_E': 500, 'SEG_X': 600,
        }
        return segments_to_vlans.get(segment)

    def _encapsulate_testing_result(self, mac, port_behavior):
        devices_state_map = {
            'device_mac_behaviors': {
                mac: {'port_behavior': port_behavior}
            }
        }
        return dict_proto(devices_state_map, DevicesState)

    def test_ports_states(self):
        """Test the port states with different signals"""
        static_device_placements = {
            '00:0Y:00:00:00:02': {'switch': 't2sw2', 'port': 1, 'connected': True},
            '00:0Z:00:00:00:03': {'switch': 't2sw3', 'port': 1, 'connected': True}
        }
        dynamic_device_placements = {
            '00:0X:00:00:00:01': {'switch': 't2sw1', 'port': 1, 'connected': True},
            '00:0A:00:00:00:04': {'switch': 't2sw4', 'port': 4, 'connected': True},
            '00:0b:00:00:00:05': {'switch': 't2sw5', 'port': 5, 'connected': True}
        }
        scheduled_ts = datetime.datetime.now() + datetime.timedelta(seconds=2)
        static_device_behaviors = {
            # not a datetime
            '00:0x:00:00:00:01': {'segment': 'SEG_A', 'auto_sequestering': 'disabled',
                                  'scheduled_sequestering_timestamp': 'apple'},
            # Past datetime. Noop
            '00:0Y:00:00:00:02': {'auto_sequestering': 'disabled',
                                  'scheduled_sequestering_timestamp': '2000-01-01T00:00:00'},
            '00:0B:00:00:00:05': {'auto_sequestering': 'disabled',
                                  'scheduled_sequestering_timestamp': scheduled_ts.isoformat()}
        }
        authentication_results = {
            '00:0X:00:00:00:01': {'segment': 'SEG_X'},
            '00:0Z:00:00:00:03': {'segment': 'SEG_C'},
            '00:0a:00:00:00:04': {'segment': 'SEG_D'},
            '00:0B:00:00:00:05': {'segment': 'SEG_E'}
        }
        testing_results = [
            ('00:0Z:00:00:00:03', 'failed'),
            ('00:0A:00:00:00:04', 'passed')
        ]
        expired_device_placements = [
            ('00:0X:00:00:00:01', ('t2sw1', 1)),
            ('00:0B:00:00:00:05', ('t2sw5', 5)),
            ('00:0B:00:00:00:05', ('t2sw5', 5)),
        ]
        unauthenticated_devices = ['00:0X:00:00:00:01', '00:0A:00:00:00:04']
        reauthenticated_device = {'00:0A:00:00:00:04': {'segment': 'SEG_D'}}

        expected_device_placements = []
        expected_device_behaviors = []
        expected_dva_states = {}

        # load static device placements
        self._load_static_device_placements(
            static_device_placements, expected_device_placements)

        # load static device behaviors
        self._load_static_device_behaviors(static_device_behaviors, expected_dva_states)

        # devices are learned
        self._learn_devices(
            dynamic_device_placements, expected_device_placements, expected_dva_states)

        # devices are authenticated
        self._authenticate_devices(
            authentication_results, expected_device_behaviors, expected_dva_states)

        # received testing results for devices
        self._receive_testing_results(
            testing_results, expected_device_behaviors, expected_dva_states)

        # devices are expired
        self._expire_devices(
            expired_device_placements, expected_device_placements, expected_dva_states)

        # devices are unauthenticated
        self._unauthenticate_devices(
            unauthenticated_devices, expected_device_behaviors, expected_dva_states)

        # devices are reauthenticated
        self._reauthenticate_devices(
            reauthenticated_device, expected_device_behaviors, expected_dva_states)

    def _load_static_device_placements(self, static_device_placements, expected_device_placements):
        for mac, device_placement_map in static_device_placements.items():
            self._port_state_manager.handle_device_placement(mac, dict_proto(
                device_placement_map, DevicePlacement), static=True)

        expected_device_placements.extend([
            # mac, connected, static
            ('00:0y:00:00:00:02', True, True),
            ('00:0z:00:00:00:03', True, True),
        ])
        self._verify_received_device_placements(expected_device_placements)

    def _load_static_device_behaviors(self, static_device_behaviors, expected_dva_states):
        for mac, device_behavior_map in static_device_behaviors.items():
            self._port_state_manager.handle_static_device_behavior(
                mac, dict_proto(device_behavior_map, DeviceBehavior))

        expected_states = {
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.UNAUTHENTICATED
        }
        self._verify_ports_states(expected_states)

        expected_dva_states.update({
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.UNAUTHENTICATED
        })
        self._verify_dva_states(expected_dva_states)
        # pylint: disable=protected-access
        self._port_state_manager._logger.error.assert_called_once_with(
            'Failed to parse scheduled sequestering timestamp: %s.', 'apple')
        self._port_state_manager._logger.warning.assert_called_once_with(
            'Ignoring past sequester timestamp %s for device %s.',
            datetime.datetime(2000, 1, 1, 0, 0, tzinfo=dateutil.tz.tzlocal()),
            '00:0y:00:00:00:02')

    def _learn_devices(self, dynamic_device_placements, expected_device_placements,
                       expected_dva_states):
        for mac, device_placement_map in dynamic_device_placements.items():
            self._port_state_manager.handle_device_placement(mac, dict_proto(
                device_placement_map, DevicePlacement), static=False)

        expected_device_placements.extend([
            ('00:0x:00:00:00:01', True, False),
            ('00:0a:00:00:00:04', True, False),
            ('00:0b:00:00:00:05', True, False)
        ])
        self._verify_received_device_placements(expected_device_placements)

        expected_dva_states.update({
            '00:0x:00:00:00:01': self.STATIC_OPERATIONAL,
            '00:0a:00:00:00:04': self.UNAUTHENTICATED,
            '00:0b:00:00:00:05': self.UNAUTHENTICATED
        })
        self._verify_dva_states(expected_dva_states)

    def _authenticate_devices(self, authentication_results, expected_device_behaviors,
                              expected_dva_states):
        for mac, device_behavior_map in authentication_results.items():
            self._port_state_manager.handle_device_behavior(
                mac, dict_proto(device_behavior_map, DeviceBehavior))

        expected_states = {
            '00:0x:00:00:00:01': self.OPERATIONAL,
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.SEQUESTERED,
            '00:0a:00:00:00:04': self.SEQUESTERED,
            '00:0b:00:00:00:05': self.OPERATIONAL
        }
        self._verify_ports_states(expected_states)

        # Device 00:0b:00:00:00:05 should be sequestered after 2s
        time.sleep(2)
        expected_states['00:0b:00:00:00:05'] = self.SEQUESTERED
        self._verify_ports_states(expected_states)

        expected_device_behaviors.extend([
            ('00:0x:00:00:00:01', 'SEG_A', True),
            ('00:0x:00:00:00:01', 'SEG_A', True),
            ('00:0z:00:00:00:03', 'TESTING', False),
            ('00:0a:00:00:00:04', 'TESTING', False),
            ('00:0b:00:00:00:05', 'SEG_E', False),
            ('00:0b:00:00:00:05', 'TESTING', False)
        ])
        self._verify_received_device_behaviors(expected_device_behaviors)

        expected_dva_states.update({
            '00:0z:00:00:00:03': self.SEQUESTERED,
            '00:0a:00:00:00:04': self.SEQUESTERED,
            '00:0b:00:00:00:05': self.SEQUESTERED
        })
        self._verify_dva_states(expected_dva_states)

    def _receive_testing_results(self, testing_results, expected_device_behaviors,
                                 expected_dva_states):
        for testing_result in testing_results:
            self._port_state_manager.handle_testing_result(
                self._encapsulate_testing_result(*testing_result))

        expected_states = {
            '00:0x:00:00:00:01': self.OPERATIONAL,
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.INFRACTED,
            '00:0a:00:00:00:04': self.OPERATIONAL,
            '00:0b:00:00:00:05': self.SEQUESTERED
        }
        self._verify_ports_states(expected_states)

        expected_device_behaviors.extend([
            ('00:0z:00:00:00:03', '', False),
            ('00:0a:00:00:00:04', 'SEG_D', False)
        ])
        self._verify_received_device_behaviors(expected_device_behaviors)

        expected_dva_states.update({
            '00:0z:00:00:00:03': self.INFRACTED,
            '00:0a:00:00:00:04': self.DYNAMIC_OPERATIONAL
        })
        self._verify_dva_states(expected_dva_states)

    def _expire_devices(self, expired_device_placements, expected_device_placements,
                        expected_dva_states):
        for expired_device_placement in expired_device_placements:
            mac = None
            switch = expired_device_placement[1][0]
            port = expired_device_placement[1][1]
            self._port_state_manager.handle_device_placement(
                mac, DevicePlacement(switch=switch, port=port), False)

        expected_device_placements.extend([
            # mac, device_placement.connected, static
            ('00:0x:00:00:00:01', False, False),
            ('00:0b:00:00:00:05', False, False)
        ])
        self._verify_received_device_placements(expected_device_placements)

        expected_dva_states.pop('00:0x:00:00:00:01')
        expected_dva_states.pop('00:0b:00:00:00:05')

        self._verify_dva_states(expected_dva_states)

    def _unauthenticate_devices(self, unauthenticated_devices, expected_device_behaviors,
                                expected_dva_states):
        for mac in unauthenticated_devices:
            self._port_state_manager.handle_device_behavior(mac, DeviceBehavior())

        expected_states = {
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.INFRACTED,
            '00:0a:00:00:00:04': self.UNAUTHENTICATED
        }
        self._verify_ports_states(expected_states)

        expected_device_behaviors.extend([('00:0a:00:00:00:04', '', False)])
        self._verify_received_device_behaviors(expected_device_behaviors)

        expected_dva_states.update({
            '00:0a:00:00:00:04': self.UNAUTHENTICATED
        })
        self._verify_dva_states(expected_dva_states)

    def _reauthenticate_devices(self, reauthenticated_device, expected_device_behaviors,
                                expected_dva_states):
        for mac, device_behavior_map in reauthenticated_device.items():
            self._port_state_manager.handle_device_behavior(
                mac, dict_proto(device_behavior_map, DeviceBehavior))

        expected_states = {
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.INFRACTED,
            '00:0a:00:00:00:04': self.SEQUESTERED
        }
        self._verify_ports_states(expected_states)

        expected_device_behaviors.extend([('00:0a:00:00:00:04', 'TESTING', False)])
        self._verify_received_device_behaviors(expected_device_behaviors)

        expected_dva_states.update({
            '00:0a:00:00:00:04': self.SEQUESTERED
        })
        self._verify_dva_states(expected_dva_states)


class FotPortStatesTestCaseWithStateMachineOverride(FotPortStatesTestCase):
    """Test access port states with overrides"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sequester_config = OrchestrationConfig.SequesterConfig(
            sequester_segment=self.SEQUESTER_SEGMENT,
            auto_sequestering='enabled',
            test_result_device_states=[
                OrchestrationConfig.SequesterConfig.TestResultDeviceStateTransition(
                    test_result="FAILED",
                    device_state="operational")
            ])
        orch_config = OrchestrationConfig(sequester_config=sequester_config)
        self._port_state_manager = PortStateManager(
            device_state_manager=self._device_state_manager,
            orch_config=orch_config)
        self._port_state_manager._logger = create_autospec(self._port_state_manager._logger)

        # All devices that were in infracted would be in operational state
        # pylint: disable=invalid-name
        self.INFRACTED = self.OPERATIONAL

    def _receive_testing_results(self, testing_results, expected_device_behaviors,
                                 expected_dva_states):
        for testing_result in testing_results:
            self._port_state_manager.handle_testing_result(
                self._encapsulate_testing_result(*testing_result))

        expected_states = {
            '00:0x:00:00:00:01': self.OPERATIONAL,
            '00:0y:00:00:00:02': self.UNAUTHENTICATED,
            '00:0z:00:00:00:03': self.OPERATIONAL,
            '00:0a:00:00:00:04': self.OPERATIONAL,
            '00:0b:00:00:00:05': self.SEQUESTERED
        }
        self._verify_ports_states(expected_states)

        expected_device_behaviors.extend([
            ('00:0z:00:00:00:03', 'SEG_C', False),
            ('00:0a:00:00:00:04', 'SEG_D', False)
        ])
        self._verify_received_device_behaviors(expected_device_behaviors)

        expected_dva_states.update({
            '00:0z:00:00:00:03': self.DYNAMIC_OPERATIONAL,
            '00:0a:00:00:00:04': self.DYNAMIC_OPERATIONAL
        })
        self._verify_dva_states(expected_dva_states)


class FotSequesterTest(IntegrationTestBase):
    """Base class for sequestering integration tests"""

    def _sequester_device(self):
        config = self._read_faucet_config()
        interface = config['dps']['nz-kiwi-t2sw1']['interfaces'][1]
        interface['native_vlan'] = 272
        self._write_faucet_config(config)
        time.sleep(5)


class FotConfigTest(FotSequesterTest):
    """Simple config change tests for fot"""

    def test_fot_sequester(self):
        """Test to check if OT trunk sequesters traffic as expected"""
        self.assertTrue(self._ping_host('forch-faux-1', '192.168.1.2'))
        self.assertFalse(self._ping_host('forch-faux-1', '192.168.2.1'))

        self._sequester_device()

        self.assertFalse(self._ping_host('forch-faux-1', '192.168.1.2'))
        self.assertTrue(self._ping_host('forch-faux-1', '192.168.2.1'))


class FotContainerTest(IntegrationTestBase):
    """Test suite for dynamic config changes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack_options['no-test'] = True
        self.stack_options['fot'] = True
        self.stack_options['dhcp'] = True
        self.stack_options['devices'] = 5

    def _internal_dhcp(self, device_container):
        def dhclient_method(container=None):
            def run_dhclient():
                try:
                    self._run_cmd('dhclient -r', docker_container=container)
                    self._run_cmd('timeout 60s dhclient', docker_container=container)
                except Exception as e:
                    print(e)
            return run_dhclient

        device_tcpdump_text = self.tcpdump_helper(
            'faux-eth0', 'src port 67', packets=2,
            funcs=[dhclient_method(container=device_container)],
            timeout=60, docker_host=device_container)

        vlan_tcpdump_text = self.tcpdump_helper(
            'data0', 'vlan and src port 67', packets=2,
            funcs=[dhclient_method(container=device_container)],
            timeout=60, docker_host='forch-controller-1')

        return device_tcpdump_text, vlan_tcpdump_text

    def _check_lldp_lacp_mirroring(self):
        lldp_eth_type = "0x88cc"
        lacp_eth_type = "0x8809"
        faux_interface = "data0"
        timeout = 60
        eth_type_filter = "ether proto "
        mirror_host = "forch-controller-1"
        lldp_tcpdump_text = self.tcpdump_helper(
            faux_interface, eth_type_filter + lldp_eth_type, packets=2,
            timeout=timeout, docker_host=mirror_host)
        self.assertTrue(lldp_eth_type in lldp_tcpdump_text)
        lacp_tcpdump_text = self.tcpdump_helper(
            faux_interface, eth_type_filter + lacp_eth_type, packets=2,
            timeout=timeout, docker_host=mirror_host)
        self.assertTrue(lacp_eth_type in lacp_tcpdump_text)

    def _check_allowed_vlans(self, vlan_tcpdump_text):
        allowed_vlan = '171'
        vlans = re.findall(r'(?<=vlan )\w+', vlan_tcpdump_text)
        no_vlan = not re.search("DHCP.*Reply", vlan_tcpdump_text)
        is_vlan_allowed = all(vlan == allowed_vlan for vlan in vlans)
        return no_vlan or is_vlan_allowed

    def test_mirroring(self):
        """Test packet mirroring for FOT setup"""
        self._check_lldp_lacp_mirroring()
        # Trigger learning event for devices to trigger their initial state
        self._run_cmd('ping -c1 -w2 8.8.8.8', docker_container='forch-faux-1', strict=False)
        self._run_cmd('ping -c1 -w2 8.8.8.8', docker_container='forch-faux-5', strict=False)
        self._check_lldp_lacp_mirroring()

    def test_dhcp_reflection(self):
        """Test to check DHCP reflection when on test VLAN"""
        # Trigger learning event for devices to trigger their initial state
        self._run_cmd('ping -c1 -w2 8.8.8.8', docker_container='forch-faux-1', strict=False)
        self._run_cmd('ping -c1 -w2 8.8.8.8', docker_container='forch-faux-5', strict=False)

        # Test DHCP reflection for sequestered device
        device_tcpdump_text, vlan_tcpdump_text = self._internal_dhcp('forch-faux-1')
        self.assertTrue(re.search("DHCP.*Reply", device_tcpdump_text))
        self.assertTrue(re.search("DHCP.*Reply", vlan_tcpdump_text))
        self.assertFalse(self._check_allowed_vlans(vlan_tcpdump_text))

        # Test (lack of) DHCP reflection for operational device
        device_tcpdump_text, vlan_tcpdump_text = self._internal_dhcp('forch-faux-4')
        self.assertTrue(re.search("DHCP.*Reply", device_tcpdump_text))
        self.assertTrue(self._check_allowed_vlans(vlan_tcpdump_text))


if __name__ == '__main__':
    unittest.main()
