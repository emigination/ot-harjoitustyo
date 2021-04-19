from .VotesTable import VotesTable
from tkinter import ttk

class StartView:

    def __init__(self, root, show_results_view):
        self._root=root
        self._show_results_view=show_results_view
        self._upframe=ttk.Frame(master=self._root)
        self._lowframe=ttk.Frame(master=self._root)
        self._tbl=VotesTable(self._root)

        title = ttk.Label(master=self._upframe, text="Äänten lasku sovellus\n")
        instructions = ttk.Label(master=self._upframe, text="\nKirjaa ehdokkaiden numerot\n")
        candidatesLabel = ttk.Label(master=self._upframe, text="Ehdokkaiden määrä:")
        votersLabel = ttk.Label(master=self._upframe, text="Äänestäjien määrä:")
        candidatesEntry=ttk.Entry(master=self._upframe)
        votersEntry=ttk.Entry(master=self._upframe)
        okButton = ttk.Button(master=self._upframe, text="Ok", command=lambda: self._ok_click(candidatesEntry.get(), votersEntry.get()))
        seatsLabel = ttk.Label(master=self._lowframe, text="Valittavien määrä:")
        seatsEntry=ttk.Entry(master=self._lowframe)
        countButton = ttk.Button(master=self._lowframe, text="Laske", command=lambda: self._count_click(seatsEntry.get()))

        title.grid(row=0, column=1)

        candidatesLabel.grid(row=2, column=1)
        candidatesEntry.grid(row=2, column=2)
        votersLabel.grid(row=3, column=1)
        votersEntry.grid(row=3, column=2)
        okButton.grid(column=2, pady=10)

        instructions.grid(column=1)

        self._upframe.pack()

        self._tbl.get_frame().pack()

        seatsLabel.grid(row=1,column=1,padx=10,pady=20)
        seatsEntry.grid(row=1,column=2)
        countButton.grid(pady=20)
        self._lowframe.pack()

    def _ok_click(self,c,v):
        self._tbl=self._tbl.expand_table(c,v)

    def _count_click(self,seats):
        results = self._tbl.count_click(seats)
        if results:
            self._upframe.destroy()
            self._lowframe.destroy()
            self._show_results_view(results)
