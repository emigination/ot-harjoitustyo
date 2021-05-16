from tkinter import ttk


class ResultsView:

    def __init__(self, root, votes, show_start_view):
        """Luokan konstrktori.

        Args:
            root: Näkymän vanhempi.
            votes: Votes-olio
            show_start_view: Funktio aloitusnäkymään palaamiseksi.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root, padding=(150,10,150,200))
        self._votes = votes
        self._show_start_view = show_start_view
        self._initialize()

    def _initialize(self):
        title = ttk.Label(master=self._frame, text="Tulokset")
        txt = ttk.Label(master=self._frame, text="Voittajat:")
        result = self._votes.stv_result()
        results_text = ttk.Label(master=self._frame, text=result.get_winners())
        return_button = ttk.Button(master=self._frame, text="Palaa", command=self._show_start_view)

        title.grid(pady=10)
        txt.grid()
        results_text.grid(sticky='N')
        return_button.grid(pady=20)

        self._frame.pack()

    def delete_view(self):
        """Poistaa näkymän.
        """
        self._frame.destroy()
