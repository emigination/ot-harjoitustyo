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
        tabletowrite = self.database.get_table(tablename)
        file = tkinter.filedialog.asksaveasfilename(
            filetypes=(('csv files', '.csv'),))
        if file in ('', None):
            return False
        return self._write_csv(tabletowrite, file)


    def _write_csv(self, table, file):
        with open(file, mode='w', newline='') as csvfile:
            votewriter = csv.writer(csvfile)
            for row in table:
                votewriter.writerow(row)
        return True
