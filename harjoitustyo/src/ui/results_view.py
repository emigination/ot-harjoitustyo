from tkinter import ttk


class ResultsView:

    def __init__(self, root, votes):
        self._root = root
        self._frame = ttk.Frame(master=self._root, padding=(150,10,150,200))
        self._votes = votes

        title = ttk.Label(master=self._frame, text="Tulokset")
        txt = ttk.Label(master=self._frame, text="Voittajat:")
        title.grid(pady=10)
        txt.grid()

        result = self._votes.stv_result()
        results_text = ttk.Label(master=self._frame, text=result.get_winners())
        results_text.grid(sticky='N')

        self._frame.pack()
