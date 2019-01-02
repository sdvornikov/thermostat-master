from unittest import TestCase

from TempSensor import Ds18b20RawData


class TestDs18b20RawData(TestCase):
    def test_valid_data(self):
        lines = ['66 01 1a ff 7f ff 0a 10 88 : crc=88 YES', '66 01 1a ff 7f ff 0a 10 88 t=22375']
        raw_data = Ds18b20RawData(lines)
        self.assertTrue(raw_data.is_valid())
        self.assertEqual(22.375, raw_data.get_temperature())

    def test_invalid_data(self):
        lines = ['invalid data']
        raw_data = Ds18b20RawData(lines)
        self.assertFalse(raw_data.is_valid())
        self.assertEqual(None, raw_data.get_temperature())
