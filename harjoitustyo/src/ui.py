from tkinter import Button, Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        title = ttk.Label(master=self._root, text="Äänten lasku sovellus\n")
        instructions = ttk.Label(master=self._root, text="\nKirjaa ehdokkaiden numerot\n")
        countbutton = ttk.Button(master=self._root, text="Laske")
        candidatesLabel = ttk.Label(master=self._root, text="Ehdokkaiden määrä:")
        votersLabel = ttk.Label(master=self._root, text="Äänestäjien määrä:")
        candidatesEntry=ttk.Entry(master=self._root)
        votersEntry=ttk.Entry(master=self._root)
        okbutton = ttk.Button(master=self._root, text="Ok")

        title.grid(row=0, column=1)

        votersLabel.grid(row=2, column=1)
        votersEntry.grid(row=2, column=2)
        candidatesLabel.grid(row=3, column=1)
        candidatesEntry.grid(row=3, column=2)
        okbutton.grid(column=2, pady=10)

        instructions.grid(column=1)

        for i in range(2):
            txt=ttk.Label(master=self._root, text=f"{i+1}. valinta")
            txt.grid(row=6, column=i+1)

        i=0
        while i<4:
            txt=ttk.Label(master=self._root, text=f"Äänestäjä {i+1}")
            txt.grid(row=7+i, column=0)
            for j in range(2):
                kentta = ttk.Entry(master=self._root)
                kentta.grid(row=7+i, column=j+1)
            i+=1


        countbutton.grid(column=1, pady=10)
