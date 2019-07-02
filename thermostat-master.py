import time
import requests
from datetime import datetime

from local_store import LocalStorage
from TempSensor import TempSensor

store = LocalStorage('thermostat.db')
temp_sensor = TempSensor()
id = store.init_sensor('ds18b20')

while True:
    t = temp_sensor.read_temp()
    print(t)
    store.log_sensor_data(id, str(t))
    payload = {'sensorId': id, 'ts': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': str(t)}
    r = requests.put("https://411o2lqb64.execute-api.us-east-1.amazonaws.com/default/writeValue", json=payload)
    time.sleep(60)
