import unittest
from tempfile import NamedTemporaryFile
from services.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.file = NamedTemporaryFile()
        self.database = Database(self.file.name)

    def test_save_table(self):
        votelist = [['1', '2'], ['', ''], ['2', '1']]
        self.database.save_table(votelist, 'testtable')
        self.assertEqual(self.database.fetch_tablenames(), ['testtable'])


