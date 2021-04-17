from tkinter import ttk
import csv

class votesTable:
    def __init__(self, root):
        self._root=root
        self._frame=ttk.Frame(master=self._root)
        self.candidates=0
        self.voters=0
        self.expandTable(3,4)

    def getFrame(self):
        return(self._frame)

    def expandTable(self,c,v):
        c=int(c)-self.candidates
        v=int(v)-self.voters
        if c>0 and v>0:
            for i in range(c):
                txt=ttk.Label(master=self._frame, text=f"{i+1+self.candidates}. valinta")
                txt.grid(row=0, column=i+self.candidates+1)
            for i in range(v):
                txt=ttk.Label(master=self._frame, text=f"Äänestäjä {i+1+self.voters}")
                txt.grid(row=i+1+self.voters, column=0)
                for j in range(c):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=i+1+self.voters, column=j+1+self.candidates)
        if c>0:
            for i in range(c):
                txt=ttk.Label(master=self._frame, text=f"{i+1+self.candidates}. valinta")
                txt.grid(row=0, column=i+self.candidates+1)
                for j in range(self.voters):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=j+1, column=i+1+self.candidates)
        if v>0:
            for i in range(v):
                txt=ttk.Label(master=self._frame, text=f"Äänestäjä {i+1+self.voters}")
                txt.grid(row=i+1+self.voters, column=0)
                for j in range(self.candidates):
                    field = ttk.Entry(master=self._frame)
                    field.grid(row=i+1+self.voters, column=j+1)

        if v<0:
            for i in range(self.voters+v+1, self.voters+1):
                for field in self._frame.grid_slaves(row=i):
                    field.grid_remove()

        if c<0:
            for i in range(self.candidates+c+1, self.candidates+1):
                for field in self._frame.grid_slaves(column=i):
                    field.grid_remove()

        self.candidates+=c
        self.voters+=v
        return(self)

    def countClick(self):
        table=[]
        for i in range(self.voters):
            table.append([])
            for j in range(self.candidates):
                table[i].append(self._frame.grid_slaves(row=i+1, column=j+1))
