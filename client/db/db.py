import sqlite3
import dbm

with dbm.open('local_database', 'c') as db:
    db['some_file'] = {
        'filepath': 'path',
        'filesha': 'sha',
    }

