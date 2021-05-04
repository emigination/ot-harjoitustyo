import csv
import tkinter.filedialog


class FileWriter:
    def __init__(self, database):
        self.database = database

    def write(self, tablename):
        table = self.database.get_table(tablename)
        file = tkinter.filedialog.asksaveasfilename(
            filetypes=(('csv files', '.csv'),))
        if file in ('', None):
            return False
        with open(file, mode='w', newline='') as csvfile:
            votewriter = csv.writer(csvfile)
            for row in table:
                votewriter.writerow(row)
        return True
