from unittest import TestCase
from local_store import LocalStorage


class TestLocalStorage(TestCase):
    def test_init_sensor_once(self):
        store = LocalStorage(':memory:')
        id = store.init_sensor('test_sensor')
        self.assertEqual(1, id)

    def test_init_sensor_existing(self):
        store = LocalStorage(':memory:')
        store.init_sensor('test_sensor')
        id = store.init_sensor('test_sensor')
        self.assertEqual(1, id)

    def test_init_two_sensors(self):
        store = LocalStorage(':memory:')
        id1 = store.init_sensor('test_sensor1')
        id2 = store.init_sensor('test_sensor2')
        self.assertEqual(1, id1)
        self.assertEqual(2, id2)

    def test_log_sensor_data(self):
        self.fail()

