import csv
import tkinter.filedialog


class FileReader:
    """Luokka, joka lukee csv-tiedostoja ja tekee niistä taulukkolistoja.

    Attributes:
        votes: Lista äänistä.
    """

    def __init__(self):
        """Luokan konstruktori.

        """
        self.votes = None

    def read(self):
        """Lukee csv-tiedoston ja luo siitä taulukkolistan.

        Returns:
            Äänitaulukko.
        """
        file = tkinter.filedialog.askopenfile(
            mode="r", filetypes=(('csv files', '.csv'),))
        if file is None:
            return None
        return self._tablify_file(file)

    def _tablify_file(self, file):
        self.votes = []
        votereader = csv.reader(file)
        for row in votereader:
            self.votes.append(row)
        return self.votes
