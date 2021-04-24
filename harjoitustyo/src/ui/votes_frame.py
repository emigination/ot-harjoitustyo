from tkinter import ttk, StringVar
from services.votes import Votes


class VotesFrame:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._candidates = 0
        self._voters = 0
        self._errormsg = StringVar()
        self._errormsg.set("")
        self._error_label = ttk.Label(master=self._frame,textvariable=self._errormsg, foreground='red')
        self.expand_table(3, 4)


    def get_frame(self):
        return self._frame

    def expand_table(self, candidates, voters):
        candidates = int(candidates)-self._candidates
        voters = int(voters)-self._voters
        if candidates > 0 and voters > 0:
            for i in range(candidates):
                txt = ttk.Label(master=self._frame,
                                text=f"{i+1+self._candidates}. valinta")
                txt.grid(row=0, column=i+self._candidates+1)
            for i in range(voters):
                txt = ttk.Label(master=self._frame,
                                text=f"Äänestäjä {i+1+self._voters}")
                txt.grid(row=i+1+self._voters, column=0)
                for j in range(candidates):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=i+1+self._voters, column=j+1+self._candidates)
        if candidates > 0:
            for i in range(candidates):
                txt = ttk.Label(master=self._frame,
                                text=f"{i+1+self._candidates}. valinta")
                txt.grid(row=0, column=i+self._candidates+1)
                for j in range(self._voters):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=j+1, column=i+1+self._candidates)
        if voters > 0:
            for i in range(voters):
                txt = ttk.Label(master=self._frame,
                                text=f"Äänestäjä {i+1+self._voters}")
                txt.grid(row=i+1+self._voters, column=0)
                for j in range(self._candidates):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=i+1+self._voters, column=j+1)

        if voters < 0:
            for i in range(self._voters+voters+1, self._voters+1):
                for field in self._frame.grid_slaves(row=i):
                    field.grid_remove()

        if candidates < 0:
            for i in range(self._candidates+candidates+1, self._candidates+1):
                for field in self._frame.grid_slaves(column=i):
                    field.grid_remove()

        self._candidates += candidates
        self._voters += voters
        self._error_label.grid()
        return self

    def count_click(self, seats):
        votes_list = []
        for i in range(self._voters):
            votes_list.append([])
            for j in range(self._candidates):
                vote = self._frame.grid_slaves(row=i+1, column=j+1)[0].get()
                votes_list[i].append(vote)
        if not seats.isnumeric() or int(seats)<=0:
            self._errormsg="Valittavien määrä ei ole positiivinen kokonaisluku"
            return False
        if int(seats)>=self._candidates:
            self._errormsg="Valittavien määrä on suurempi tai yhtä suuri kuin ehdokkaiden"
            return False
        votes = Votes(votes_list, int(seats), self._candidates)
        errorslist=votes.check_validity()
        if len(errorslist)>0:
            errors=""
            for error in errorslist:
                errors=errors+error+'\n'
            self._errormsg=errors
            return False
        self._frame.destroy()
        return votes
