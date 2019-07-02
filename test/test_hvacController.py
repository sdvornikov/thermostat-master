from unittest import TestCase
from unittest.mock import Mock


from hvac_controller import HvacController, FanMode


class TestHvacController(TestCase):

    def setUp(self):
        self.heat_relay = Mock()
        self.ac_relay = Mock()
        self.fan_relay = Mock()
        self.controller = HvacController(self.heat_relay, self.fan_relay, self.ac_relay)

    def test_hvac_state(self):
        self.controller.fan_state = FanMode.ON
        self.fan_relay.on.assert_called_once_with()
        self.ac_relay.off.assert_called_once_with()
        self.heat_relay.off.assert_called_once_with()
