import unittest
import csv
from tempfile import NamedTemporaryFile
from services.file_reader import FileReader

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.filereader=FileReader()
        self.file = NamedTemporaryFile()
        votelist = [['1', '2'], ['', ''], ['2', '1']]
        with open(self.file.name, mode='w', newline='') as csvfile:
            votewriter = csv.writer(csvfile)
            for row in votelist:
                votewriter.writerow(row)

    def test_read_csv(self):
        with open(self.file.name) as file:
            readfile = self.filereader._tablify_file(file)
            self.assertEqual(readfile, [['1', '2'], ['', ''], ['2', '1']])
