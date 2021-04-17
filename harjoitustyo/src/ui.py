from votesTable import votesTable
from tkinter import ttk

class UI:
    def __init__(self, root):
        self._root = root
        self._frame=ttk.Frame(master=self._root)
        self._tbl=None

    def start(self):
        title = ttk.Label(master=self._frame, text="Äänten lasku sovellus\n")
        instructions = ttk.Label(master=self._frame, text="\nKirjaa ehdokkaiden numerot\n")
        countbutton = ttk.Button(master=self._root, text="Laske")
        candidatesLabel = ttk.Label(master=self._frame, text="Ehdokkaiden määrä:")
        votersLabel = ttk.Label(master=self._frame, text="Äänestäjien määrä:")
        candidatesEntry=ttk.Entry(master=self._frame)
        votersEntry=ttk.Entry(master=self._frame)
        okbutton = ttk.Button(master=self._frame, text="Ok", command=lambda: self._okButtonClick(candidatesEntry.get(), votersEntry.get()))
        self.tbl = votesTable(self._root)

        title.grid(row=0, column=1)

        candidatesLabel.grid(row=2, column=1)
        candidatesEntry.grid(row=2, column=2)
        votersLabel.grid(row=3, column=1)
        votersEntry.grid(row=3, column=2)
        okbutton.grid(column=2, pady=10)

        instructions.grid(column=1)

        self._frame.pack()

        self.tbl.getFrame().pack()

        countbutton.pack()

    def _okButtonClick(self,c,v):
        self.tbl=self.tbl.expandTable(c,v)