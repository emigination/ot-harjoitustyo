import sqlite3
import os


class Database:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.database = sqlite3.connect(os.path.join(
            dirname, "..", "..", "data", "database.sqlite"))

    def save_table(self, votetable, tablename):
        try:
            self.database.execute("create table " + tablename +
                            "(id integer primary key, voter integer," + \
                         " choiceno integer, candidate text)")
            self.database.execute("begin")
            for (index, voter) in enumerate(votetable):
                for (index2, choice) in enumerate(voter):
                    self.database.execute(
                        "INSERT INTO " + tablename + " (voter, choiceno, candidate)" + \
                         "VALUES (?, ?, ?)", [index, index2, choice])
            self.database.execute("commit")
            return True
        except:
            return False

    def fetch_tablenames(self):
        return(self.database.execute("SELECT name FROM sqlite_master WHERE type='table';"))
