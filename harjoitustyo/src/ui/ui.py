from .start_view import StartView
from .results_view import ResultsView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _show_start_view(self):
        self._current_view = StartView(self._root, self._show_results_view)

    def _show_results_view(self, votes):
        self._current_view = ResultsView(self._root, votes)
