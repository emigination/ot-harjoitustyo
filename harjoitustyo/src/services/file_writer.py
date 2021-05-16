import csv
import tkinter.filedialog


class FileWriter:
    """Kirjoittaa äänitaulukoista csv-tiedostoja.

    Attributes:
        database: Database-luokan olio, jolla on yhteys tietokantaan.
    """

    def __init__(self, database):
        """Luokan konstruktori.

        Args:
            database: Database-luokan olio.
        """
        self.database = database

    def write(self, tablename):
        """Vie tietokantatauluja csv-tiedostoina.

        Args:
            tablename: Tietokantataulun nimi.

        Returns:
            True, jos tiedoston tallennus onnistui, muuten False.
        """
        file = tkinter.filedialog.asksaveasfilename(
            filetypes=(('csv files', '.csv'),))
        if file in ('', None):
            return False
        return self._write_csv(tablename, file)


    def _write_csv(self, tablename, file):
        tabletowrite = self.database.get_table(tablename)
        with open(file, mode='w', newline='') as csvfile:
            votewriter = csv.writer(csvfile)
            for row in tabletowrite:
                votewriter.writerow(row)
        return True
