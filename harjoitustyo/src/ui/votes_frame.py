from tkinter import ttk, StringVar
from services.file_reader import FileReader


class VotesFrame:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self.candidates = 0
        self._voters = 0
        self._stringvarlist = []
        self.expand_table(3, 4)

    def get_frame(self):
        return self._frame

    def destroy_frame(self):
        self._frame.destroy()

    def read_file(self):
        file_reader = FileReader()
        voteslist = file_reader.read()
        if voteslist is None:
            return None
        lengthlist = [len(vote) for vote in voteslist]
        candidates=max(lengthlist)
        self.expand_table(candidates, len(voteslist))
        for row in range(self._voters):
            for column in range(len(voteslist[row])):
                self._stringvarlist[row][column].set(voteslist[row][column])
        return(candidates, len(voteslist))

    def _insert_field(self, y_coordinate, x_coordinate):
        if len(self._stringvarlist) < y_coordinate:
            self._stringvarlist.append([])
        stringvariable = StringVar(self._frame)
        self._stringvarlist[y_coordinate-1].append(stringvariable)
        ttk.Entry(master=self._frame, textvariable=stringvariable,
                  width=10).grid(row=y_coordinate, column=x_coordinate)

    def expand_table(self, candidates, voters):
        candidates = int(candidates)-self.candidates
        voters = int(voters)-self._voters
        if candidates > 0 and voters > 0:
            for i in range(candidates):
                txt = ttk.Label(master=self._frame,
                                text=f"{i+1+self.candidates}. valinta")
                txt.grid(row=0, column=i+self.candidates+1)
            for i in range(voters):
                txt = ttk.Label(master=self._frame,
                                text=f"Äänestäjä {i+1+self._voters}")
                txt.grid(row=i+1+self._voters, column=0)
                for j in range(candidates):
                    self._insert_field(i+1+self._voters, j+1+self.candidates)
        if candidates > 0:
            for i in range(candidates):
                txt = ttk.Label(master=self._frame,
                                text=f"{i+1+self.candidates}. valinta")
                txt.grid(row=0, column=i+self.candidates+1)
                for j in range(self._voters):
                    self._insert_field(j+1, i+1+self.candidates)
        if voters > 0:
            for i in range(voters):
                txt = ttk.Label(master=self._frame,
                                text=f"Äänestäjä {i+1+self._voters}")
                txt.grid(row=i+1+self._voters, column=0)
                for j in range(self.candidates):
                    self._insert_field(i+1+self._voters, j+1)
        if voters < 0:
            for i in range(self._voters+voters+1, self._voters+1):
                for field in self._frame.grid_slaves(row=i):
                    field.grid_remove()
            while len(self._stringvarlist) > self._voters+voters:
                self._stringvarlist.pop()
        if candidates < 0:
            for i in range(self.candidates+candidates+1, self.candidates+1):
                for field in self._frame.grid_slaves(column=i):
                    field.grid_remove()
            for row in self._stringvarlist:
                while len(row) > self.candidates+candidates:
                    row.pop()

        self.candidates += candidates
        self._voters += voters

    def tablify(self):
        votes_list = []
        for i in range(self._voters):
            votes_list.append([])
            for j in range(self.candidates):
                vote = self._frame.grid_slaves(row=i+1, column=j+1)[0].get()
                votes_list[i].append(vote)
        return votes_list
