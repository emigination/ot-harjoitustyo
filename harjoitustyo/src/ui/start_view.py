from tkinter import ttk, StringVar
from .votes_frame import VotesFrame


class StartView:

    def __init__(self, root, show_results_view):
        self._root = root
        self._show_results_view = show_results_view
        self._upframe = ttk.Frame(master=self._root)
        self._lowframe = ttk.Frame(master=self._root)
        self._votesframe = VotesFrame(self._root)
        self._errormsg = StringVar()
        self._errormsg.set("")

        title = ttk.Label(master=self._upframe, text="Vaalituloslaskuri\n")
        instructions = ttk.Label(master=self._upframe,
                                 text="\nKirjaa ehdokkaiden numerot\n")
        candidates_label = ttk.Label(
            master=self._upframe, text="Ehdokkaiden määrä:")
        voters_label = ttk.Label(master=self._upframe,
                                 text="Äänestäjien määrä:")
        candidates_entry = ttk.Entry(master=self._upframe)
        voters_entry = ttk.Entry(master=self._upframe)
        ok_button = ttk.Button(master=self._upframe, text="Ok", command=lambda: self._ok_click(
            candidates_entry.get(), voters_entry.get()))
        error_label = ttk.Label(master=self._upframe,textvariable=self._errormsg, foreground='red')
        seats_label = ttk.Label(master=self._lowframe,
                                text="Valittavien määrä:")
        seats_entry = ttk.Entry(master=self._lowframe)
        count_button = ttk.Button(master=self._lowframe, text="Laske",
                                  command=lambda: self._count_click(seats_entry.get()))

        title.grid(row=0, column=1)

        candidates_label.grid(row=2, column=1)
        candidates_entry.grid(row=2, column=2)
        voters_label.grid(row=3, column=1)
        voters_entry.grid(row=3, column=2)
        error_label.grid(row=4,column=1)
        ok_button.grid(row=4,column=2, pady=10)

        instructions.grid(column=1)

        self._upframe.pack()

        self._votesframe.get_frame().pack()

        seats_label.grid(row=1, column=1, padx=10, pady=20)
        seats_entry.grid(row=1, column=2)
        count_button.grid(pady=20)
        self._lowframe.pack()

    def _ok_click(self, candidates, voters):
        if not candidates.isnumeric() or not voters.isnumeric() or int(candidates)<=0 or int(voters)<=0:
            self._errormsg.set("Määrä ei ole positiivinen kokonaisluku")
        else:
            self._errormsg.set("")
            self._votesframe=self._votesframe.expand_table(candidates, voters)

    def _count_click(self, seats):
        results = self._votesframe.count_click(seats)
        if results:
            self._upframe.destroy()
            self._lowframe.destroy()
            self._show_results_view(results)
