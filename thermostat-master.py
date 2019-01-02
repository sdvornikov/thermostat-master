import time

from local_store import LocalStorage
from TempSensor import TempSensor

store = LocalStorage('/home/pi/thermostat.db')
temp_sensor = TempSensor()
id = store.init_sensor('ds18b20')

while True:
    t = temp_sensor.read_temp()
    print(t)
    store.log_sensor_data(id, str(t))
    time.sleep(60)
