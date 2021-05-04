from tkinter import ttk, StringVar
from services.database import Database

class SavedTablesView:

    def __init__(self, root, show_start_view):
        self._root = root
        self._show_start_view = show_start_view
        self._frame = ttk.Frame(master=self._root, padding=(50,10,50,200))
        self._database = Database()

        title = ttk.Label(master=self._frame, text="Tallennetut äänitaulukot")
        txt = ttk.Label(master=self._frame, text="Valitse taulukko")

        options =  self._database.fetch_tablenames()
        self._tablename = StringVar(self._frame, "Taulukot")
        menu = ttk.OptionMenu(self._frame, self._tablename, *options)
        view_button = ttk.Button(self._frame, text="Näytä", command=self._show_table)
        remove_button = ttk.Button(self._frame, text="Poista", command=self._remove_table)
        export_button = ttk.Button(self._frame, text="Vie csv-tiedostona", command=self._export_file)

        title.grid(column=1,pady=10)
        txt.grid(pady=10)
        menu.grid(column=1,row=1, pady=20)
        remove_button.grid(column=0,row=2)
        view_button.grid(column=1,row=2)
        export_button.grid(column=2,row=2)

        self._frame.pack()

    def _show_table(self):
        votestable = self._database.get_table(self._tablename.get())
        self._show_start_view(votestable)

    def _remove_table(self):
        return

    def _export_file(self):
        return

    def delete_view(self):
        self._frame.destroy()