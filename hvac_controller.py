from enum import Enum


class FanMode(Enum):
    AUTO = 1
    ON = 2


class HvacMode(Enum):
    OFF = 1
    HEATING = 2
    COOLING = 3


class HvacController:

    def __init__(self, heat_relay, fan_relay, ac_relay):
        self._heat_relay = heat_relay
        self._fan_relay = fan_relay
        self._ac_relay = ac_relay
        self._hvac_state = HvacMode.OFF
        self._fan_state = FanMode.AUTO

    @property
    def hvac_state(self):
        return self._hvac_state

    @hvac_state.setter
    def hvac_state(self, hvac_mode):
        self._apply_state(hvac_mode, self.fan_state)
        self._hvac_state = hvac_mode

    @property
    def fan_state(self):
        return self._fan_state

    @fan_state.setter
    def fan_state(self, fan_mode):
        self._apply_state(self.hvac_state, fan_mode)
        self._fan_state = fan_mode

    def _apply_state(self, hvac_mode, fan_mode):
        if hvac_mode is HvacMode.OFF:
            self._heat_relay.off()
            self._ac_relay.off()
            if fan_mode is FanMode.AUTO:
                self._fan_relay.off()
            else:
                self._fan_relay.on()
        elif hvac_mode is HvacMode.COOLING:
            self._heat_relay.off()
            self._ac_relay.on()
            self._fan_relay.on()
        elif hvac_mode is HvacMode.HEATING:
            self._ac_relay.off()
            self._heat_relay.on()
            self._fan_relay.on()

