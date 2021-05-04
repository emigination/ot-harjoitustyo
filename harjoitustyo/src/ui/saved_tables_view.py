from tkinter import ttk


class SavedTablesView:

    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root, padding=(150,10,150,200))
        title = ttk.Label(master=self._frame, text="Tallennetut äänitaulukot")
        title.grid(pady=10)

        self._frame.pack()