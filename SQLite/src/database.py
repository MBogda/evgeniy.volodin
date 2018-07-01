import sqlite3


class Database:
    def __init__(self, filename):
        self.filename = filename
        # only one connection - don't use with multiple threads!
        self.conn = sqlite3.connect(self.filename,
                                    detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.conn.cursor()
        self.cur.execute('PRAGMA foreign_keys = ON;')

    def create(self):
        with open('src/create_db.sql', 'r') as f:
            self.cur.executescript(f.read())
        self.conn.commit()

    def check_created(self):
        tables = {
            tbl_name for (tbl_name,) in self.cur.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }
        if tables != {'State', 'Direction', 'City', 'Observation'}:
            # todo: move literal string to variable
            raise sqlite3.OperationalError('Inappropriate database file.')

    def close(self):
        self.conn.close()

    def select_states(self):
        return {
            id_: value for (id_, value) in
            self.cur.execute('SELECT id, value FROM State').fetchall()
        }

    def select_directions(self):
        return {
            id_: value for (id_, value) in
            self.cur.execute('SELECT id, value FROM Direction').fetchall()
        }

    def select_cities(self):
        return {
            id_: value for (id_, value) in
            self.cur.execute('SELECT id, value FROM City').fetchall()
        }

    def insert_city(self, city_name):
        self.cur.execute('INSERT INTO City(value) VALUES (?)', (city_name,))
        self.conn.commit()
        return self.cur.lastrowid

    def delete_city(self, city_id):
        self.cur.execute('DELETE FROM City WHERE id = ?', (city_id,))
        self.conn.commit()

    def select_observations(self):
        return {
            values[0]: values[1:] for values in
            self.cur.execute(
                'SELECT id, datetime, city, state, temperature, '
                'precipitation, pressure, wind_direction, wind_value '
                'FROM Observation'
            ).fetchall()
        }

    def insert_observation(
            self, time=None, city=None, state=None, temperature=None,
            precipitation=None, pressure=None, wind_direction=None,
            wind_value=None
    ):
        self.cur.execute(
            'INSERT INTO Observation(datetime, city, state, temperature, '
            'precipitation, pressure, wind_direction, wind_value) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (time, city, state, temperature, precipitation, pressure,
             wind_direction, wind_value)
        )
        self.conn.commit()
        return self.cur.lastrowid

    def delete_observation(self, observation_id):
        self.cur.execute(
            'DELETE FROM Observation WHERE id = ?',
            (observation_id,)
        )
        self.conn.commit()
