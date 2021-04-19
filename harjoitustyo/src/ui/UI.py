from tkinter import ttk
from .StartView import StartView
from .ResultsView import ResultsView

class UI:
    def __init__(self, root):
        self._root=root
        self._currentView=None

    def start(self):
        self._show_start_view()

    def _show_start_view(self):
        self._currentView=StartView(self._root, self._show_results_view)

    def _show_results_view(self, votes):
        self._currentView=ResultsView(self._root, votes)
