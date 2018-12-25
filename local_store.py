import sqlite3
from sqlite3 import Error

sql_create_sensors_table = """ CREATE TABLE IF NOT EXISTS sensor (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                ); """

sql_create_data_table = """ CREATE TABLE IF NOT EXISTS data (
                                    id integer PRIMARY KEY,
                                    data text NOT NULL,
                                    ts text NOT NULL,
                                    sensor_id integer NOT NULL,
                                    FOREIGN KEY(sensor_id) REFERENCES sensor(id)
                                ); """


class LocalStorage:

    def __init__(self, db_file):
        self.__conn = self.create_connection(db_file)
        self.create_table(sql_create_sensors_table)
        self.create_table(sql_create_data_table)

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.__conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def init_sensor(self, name):
        """ creates a record for the sensor.
        :param name: sensor's name
        :return: sensor id
        """
        try:
            c = self.__conn.cursor()
            c.execute('SELECT * FROM sensor WHERE name=?', (name,))
            row = c.fetchone()
            if row is None:
                c.execute('INSERT INTO sensor (name) VALUES (?)', (name,))
                return c.lastrowid
            return row[0]
        except Error as e:
            print(e)

    def log_sensor_data(self, sensor_id, data):
        try:
            c = self.__conn.cursor()
            c.execute('INSERT (?, now(), ?) INTO sensor', (data,sensor_id))
        except Error as e:
            print(e)

    def create_connection(self, file_name):
        try:
            conn = sqlite3.connect(file_name)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)

        return None
