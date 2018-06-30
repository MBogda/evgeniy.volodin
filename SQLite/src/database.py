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