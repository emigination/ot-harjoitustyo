import sqlite3
import os


class Database:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.db = sqlite3.connect(os.path.join(
            dirname, "..", "..", "data", "database.sqlite"))

    def save_table(self, votetable, tablename):
        try:
            self.db.execute("create table " + tablename +
                            "(id integer primary key, voter integer, choiceno integer, candidate text)")
            self.db.execute("begin")
            for voter in range(len(votetable)):
                for choice in range(len(votetable[voter])):
                    self.db.execute("INSERT INTO " + tablename + " (voter, choiceno, candidate) VALUES (?, ?, ?)", [
                                    voter, choice, votetable[voter][choice]])
            self.db.execute("commit")
            return True
        except:
            return False
