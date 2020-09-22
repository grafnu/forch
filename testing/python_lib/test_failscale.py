"""Integration test base class for Forch"""
import unittest
import time

from integration_base import IntegrationTestBase


class FailScaleConfigTest(IntegrationTestBase):
    """Test suite for failure modes during scaling"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.STACK_OPTIONS.update({
            'devices': 5,
            'switches': 9,
            'mode': 'scale'
        })

    def test_stack_connectivity(self):
        """Test to build stack and check for connectivity"""
        self.assertEqual(10, self._ping_host('forch-faux-8', '192.168.1.0', count=10, output=True),
                         'warm-up ping count')
        print('x')
        process = self._ping_host_process('forch-faux-8', '192.168.1.0', count=60)
        print('a')
        time.sleep(5)
        print('b')
        self._fail_egress_link()
        print('c')
        ping_count = self._ping_host_reap(process, output=True)
        print('d')
        self._run_cmd('bin/dump_logs')
        self.assertTrue(ping_count > 25 and ping_count < 55, 'disrupted ping count %s' % ping_count)
        print('e')


if __name__ == '__main__':
    unittest.main()
