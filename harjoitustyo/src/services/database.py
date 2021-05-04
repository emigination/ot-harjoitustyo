import sqlite3
import os


class Database:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self._database = sqlite3.connect(os.path.join(
            dirname, "..", "..", "data", "database.sqlite"))

    def save_table(self, votetable, tablename):
        try:
            self._database.execute("begin;")
            self._database.execute("create table " + tablename +
                                   "(id integer primary key, voter integer," +
                                   " choiceno integer, candidate text);")
            for (index, voter) in enumerate(votetable):
                for (index2, choice) in enumerate(voter):
                    self._database.execute(
                        "INSERT INTO " + tablename + " (voter, choiceno, candidate)" +
                        "VALUES (?, ?, ?);", [index, index2, choice])
            self._database.execute("commit;")
            return True
        except:
            return False

    def fetch_tablenames(self):
        tablenames = []
        for name in self._database.execute("SELECT name FROM sqlite_master WHERE type='table';"):
            tablenames.append(name[0])
        return tablenames

    def get_table(self, tablename):
        table = []
        for row in self._database.execute("SELECT voter, choiceno, candidate FROM " +
            tablename + ";"):
            table.append(row)
        voters = table[len(table)-1][0]+1
        votestable = [[] for _ in range(voters)]
        for row in table:
            votestable[row[0]].append(row[2])
        return votestable

    def remove_table(self, tablename):
        self._database.execute("drop table " + tablename + ";")
