import csv
import tkinter.filedialog


class FileReader:
    def __init__(self):
        self.votes = None

    def read(self):
        file = tkinter.filedialog.askopenfile(
            mode="r", filetypes=(('csv files', '.csv'),))
        if file is None:
            return None
        voteslist = []
        votereader = csv.reader(file)
        for row in votereader:
            voteslist.append(row)
        return voteslist
