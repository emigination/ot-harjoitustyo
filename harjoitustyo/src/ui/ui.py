from .start_view import StartView
from .results_view import ResultsView
from .saved_tables_view import SavedTablesView
# from kokeilut.kokeilustartview import StartView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _show_start_view(self, votes=None):
        if self._current_view:
            self._current_view.delete_view()
        self._current_view = StartView(self._root, self._show_results_view, self._show_saved_tables_view, votes)

    def _show_results_view(self, votes):
        self._current_view.delete_view()
        self._current_view = ResultsView(self._root, votes, self._show_start_view)

    def _show_saved_tables_view(self):
        self._current_view.delete_view()
        self._current_view = SavedTablesView(self._root, self._show_start_view)
