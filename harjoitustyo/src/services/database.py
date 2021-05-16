import sqlite3
import os
from dotenv import load_dotenv


class Database:
    """Luokka, joka vastaa tietokantatoiminnoista.

    Attributes:
        database: Tietokannan sijainti.
    """

    def __init__(self, database_name=None):
        """Luokan konstruktori, joka luo yhteyden tietokantaan.

        Args:
            Tietokannan nimi. Jos sitä ei ole, käytetään oletustietokantaa.
        """
        dirname = os.path.dirname(__file__)
        if not database_name:
            try:
                load_dotenv(dotenv_path=os.path.join(dirname, "..", "..", ".env"))
            except FileNotFoundError:
                pass
            database_name = os.getenv('DATABASE_NAME') or 'database.sqlite'
        self._database = sqlite3.connect(os.path.join(
            dirname, "..", "..", "data", database_name))

    def save_table(self, votetable, tablename):
        """Tallentaa äänitaulukon tietokantaan.

        Args:
            votetable: Äänet kaksiulotteisena taulokkona.
            tablename: Tietokantataulun, johon äänet tallennetaan, nimi.

        Returns:
            True, jos tallentaminen onnistuu, muuten False.
        """
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
        """Hakee tietokannassa olevien taulujen nimet.

        Returns:
            Lista taulujen nimistä.
        """
        tablenames = []
        for name in self._database.execute("SELECT name FROM sqlite_master WHERE type='table';"):
            tablenames.append(name[0])
        return tablenames

    def get_table(self, tablename):
        """Hakee äänitaulun tietokannasta.

        Args:
            tablename: haettavan taulun nimi.

        Returns:
            Äänet kaksiulotteisena taulukkona.
        """
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
        """Poistaa taulun tietokannasta.

        Args:
            tablename: Poistettavan taulun nimi.
        """
        self._database.execute("drop table " + tablename + ";")
