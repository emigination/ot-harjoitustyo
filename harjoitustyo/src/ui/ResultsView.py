from .VotesTable import VotesTable
from tkinter import ttk

class ResultsView:

    def __init__(self, root, votes):
        self._root=root
        self._frame=ttk.Frame(master=self._root)
        self._votes=votes

        title = ttk.Label(master=self._frame, text="Äänten lasku sovellus\n")
        txt=ttk.Label(master=self._frame, text="Tulokset:")
        title.grid()
        txt.grid()

        self._frame.pack()

        self._votes.stv_result()
