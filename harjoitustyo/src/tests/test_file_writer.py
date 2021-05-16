import unittest
import csv
from tempfile import NamedTemporaryFile
from services.file_writer import FileWriter
from services.file_reader import FileReader
from services.database import Database

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.file = NamedTemporaryFile()
        votelist = [['2', '1'], ['1', '2']]
        database = Database(self.file.name)
        database.save_table(votelist, 'testtable')
        self.filewriter = FileWriter(database)
        self.csvfile = NamedTemporaryFile()

    def test_write_csv(self):
        with open(self.csvfile.name):
            self.filewriter._write_csv('testtable', self.csvfile.name)
        with open(self.csvfile.name) as file:
            writtentable = FileReader()._tablify_file(file)
        self.assertEqual(writtentable, [['2', '1'], ['1', '2']])
