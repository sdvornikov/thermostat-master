import os
import glob
import time


class TempSensor:

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def _read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        raw_data = Ds18b20RawData(self._read_temp_raw())
        while not raw_data.is_valid():
            time.sleep(0.2)
            raw_data = Ds18b20RawData(self._read_temp_raw())
        return raw_data.get_temperature()


class Ds18b20RawData:
    def __init__(self, raw_lines):
        self._raw_lines = raw_lines

    def is_valid(self):
        return self._raw_lines[0].strip()[-3:] == 'YES'

    def get_temperature(self):
        equals_pos = self._raw_lines[1].find('t=')
        if equals_pos != -1:
            temp_string = self._raw_lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
