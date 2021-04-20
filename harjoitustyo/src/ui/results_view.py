from tkinter import ttk


class ResultsView:

    def __init__(self, root, votes):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._votes = votes

        title = ttk.Label(master=self._frame, text="Tulokset")
        txt = ttk.Label(master=self._frame, text="Voittajat:")
        title.grid()
        txt.grid(pady=10)

        result = self._votes.stv_result()
        results_text = ttk.Label(master=self._frame, text=result.get_winners())
        results_text.grid()

        self._frame.pack()
