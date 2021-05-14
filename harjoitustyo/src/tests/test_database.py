import unittest
from tempfile import NamedTemporaryFile
from services.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.file = NamedTemporaryFile()
        self.database = Database(self.file.name)
        votelist = [['2', '1'], ['1', '2']]
        self.database.save_table(votelist, 'testtable')

    def test_save_table(self):
        votelist = [['1', '2'], ['', ''], ['2', '1']]
        self.database.save_table(votelist, 'anothertesttable')
        self.assertIn('anothertesttable', self.database.fetch_tablenames())

    def test_fetch_table(self):
        table = self.database.get_table('testtable')
        self.assertEqual(table, [['2', '1'], ['1', '2']])

    def test_remove_table(self):
        self.database.remove_table('testtable')
        self.assertNotIn('testtable', self.database.fetch_tablenames())
