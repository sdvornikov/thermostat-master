import RPi.GPIO as GPIO


class Relay:
    def __init__(self, pin, default_state=False):
        self.pin = pin
        self._state = default_state
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(self.pin, default_state)

    @property
    def state(self):
        return self._state

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self._state = True

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self._state = False
