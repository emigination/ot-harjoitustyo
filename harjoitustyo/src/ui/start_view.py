from tkinter import ttk, StringVar
from .votes_frame import VotesFrame
from services.votes import Votes


class StartView:

    def __init__(self, root, show_results_view):
        self._root = root
        self._show_results_view = show_results_view
        self._upframe = ttk.Frame(master=self._root)
        self._lowframe = ttk.Frame(master=self._root)
        self._votesframe = VotesFrame(self._root)
        self._errormsg = StringVar(self._upframe)
        self._vote_check_msg = StringVar(self._lowframe)
        self._candidates_number = StringVar(self._upframe, '3')
        self._voters_number = StringVar(self._upframe, '4')
        self.seats_entry = ttk.Entry(master=self._lowframe)

        title = ttk.Label(master=self._upframe, text="Vaalituloslaskuri\n")
        entry_instructions = ttk.Label(master=self._upframe,
                                       text="\nKirjaa ehdokkaiden numerot tai lue \n")
        file_button = ttk.Button(
            master=self._upframe, text="csv-tiedosto*", command=self._file_click)
        file_instructions = ttk.Label(
            master=self._upframe, text="*csv-tiedostossa tulee olla vain numeroita, ei esim. otsikoita\n")
        candidates_label = ttk.Label(
            master=self._upframe, text="Ehdokkaiden määrä:")
        voters_label = ttk.Label(master=self._upframe,
                                 text="Äänestäjien määrä:")
        candidates_entry = ttk.Entry(
            master=self._upframe, textvariable=self._candidates_number)
        voters_entry = ttk.Entry(master=self._upframe,
                                 textvariable=self._voters_number)
        ok_button = ttk.Button(master=self._upframe, text="Ok", command=lambda: self._ok_click(
            candidates_entry.get(), voters_entry.get()))
        error_label = ttk.Label(
            master=self._upframe, textvariable=self._errormsg, foreground='red')

        seats_label = ttk.Label(master=self._lowframe,
                                text="Valittavien määrä:")
        vote_check_label = ttk.Label(
            master=self._lowframe, textvariable=self._vote_check_msg, foreground='red')
        count_button = ttk.Button(master=self._lowframe, text="Laske",
                                  command=self._count_click)
        save_button = ttk.Button(master=self._lowframe, text="Tallenna äänet...",
                                 command=self._save_click)

        title.grid(row=0, column=1)

        candidates_label.grid(row=2, column=1)
        candidates_entry.grid(row=2, column=2)
        voters_label.grid(row=3, column=1)
        voters_entry.grid(row=3, column=2)
        error_label.grid(row=4, column=1)
        ok_button.grid(row=4, column=2, pady=10)

        entry_instructions.grid(column=1, sticky="E")
        file_button.grid(row=5, column=2, sticky="W")
        file_instructions.grid(row=6, columnspan=3, padx=20)

        self._upframe.pack()

        self._votesframe.get_frame().pack()

        seats_label.grid(row=1, column=1, padx=10, pady=10)
        self.seats_entry.grid(row=1, column=2)
        vote_check_label.grid(row=2, column=1)
        count_button.grid(column=1, pady=10)
        save_button.grid(row=3, column=2, pady=10)
        self._lowframe.pack()

    def _ok_click(self, candidates, voters):
        self._candidates_number.set(candidates)
        self._voters_number.set(voters)
        if not candidates.isnumeric() or not voters.isnumeric() or int(candidates) <= 0 or int(voters) <= 0:
            self._errormsg.set("Määrä ei ole positiivinen kokonaisluku")
        else:
            self._errormsg.set("")
            self._votesframe = self._votesframe.expand_table(
                candidates, voters)

    def _file_click(self):
        numbers = self._votesframe.read_file()
        if numbers is None:
            return
        self._candidates_number.set(numbers[0])
        self._voters_number.set(numbers[1])

    def _create_votes_object(self):
        self._vote_check_msg.set("")
        votes = Votes(self._votesframe.tablify(), self.seats_entry.get(),
                      self._votesframe.candidates)
        errorslist = votes.check_validity()
        if len(errorslist) > 0:
            errors = ""
            for error in errorslist:
                errors = errors+error+'\n'
            self._vote_check_msg.set(errors)
            return False
        return votes

    def _count_click(self):
        votes = self._create_votes_object()
        if votes:
            self._upframe.destroy()
            self._votesframe.destroy_frame()
            self._lowframe.destroy()
            self._show_results_view(votes)

    def _save_click(self):
        savingframe = ttk.Frame(master=self._root)
        name_instruction = ttk.Label(master=savingframe, text="Anna nimi äänitaulukolle:")
        name_entry = ttk.Entry(master=savingframe)
        save_named_button = ttk.Button(master=savingframe, text="Tallenna",
                                       command=lambda: self._save_named(name_entry.get()))
        cancel_button = ttk.Button(master=savingframe, text="Peruuta",
                                   command=lambda: self._delete_frame(savingframe))
        name_instruction.grid(pady=10)
        name_entry.grid(column=1, row=0)
        cancel_button.grid(pady=10)
        save_named_button.grid(column=1, row=1)
        savingframe.pack()

    def _delete_frame(self,frame):
        frame.destroy()

    def _save_named(self, name):
        votes = self._create_votes_object()
        # if votes:
        #     saved = votes.save()
        #     if saved:
        #         self._vote_check_msg.set("Tallennus onnistui")
        #     else:
        #         self._vote_check_msg.set("Tallennus epäonnistui")
