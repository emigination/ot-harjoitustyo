#https://gist.github.com/bhaskar-nair2/94b2d4dd511a1cd38ecde9c9481c4b28 used as reference

from tkinter import Scrollbar, Frame, Canvas, RIGHT, VERTICAL, TRUE, BOTH, NW, X, Y, HORIZONTAL, BOTTOM

class ScrollableFrame(Frame):

    def __init__(self, root, *args, **kw):

        Frame.__init__(self, root, *args, **kw)
        vertical_scrollbar = Scrollbar(self, orient=VERTICAL)
        horizontal_scrollbar = Scrollbar(self, orient=HORIZONTAL)
        self.canvas = Canvas(self, yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
        self.interior = Frame(self.canvas)

        vertical_scrollbar.pack(fill=Y, side=RIGHT)
        horizontal_scrollbar.pack(fill=X, side=BOTTOM)
        self.canvas.pack(fill=BOTH, expand=TRUE)
        vertical_scrollbar.config(command=self.canvas.yview)
        horizontal_scrollbar.config(command=self.canvas.xview)
        self.canvas.create_window(0, 0, window=self.interior, anchor=NW)

        def _mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.bind_all("<MouseWheel>", _mousewheel)

        def _configure_interior(event):
            self.canvas.config(
                scrollregion=f"0 0 {self.interior.winfo_reqwidth()} {self.interior.winfo_reqheight()}")
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.interior.winfo_reqwidth())
            if self.interior.winfo_reqheight() != self.canvas.winfo_height():
                self.canvas.config(height=self.interior.winfo_reqheight())

        self.interior.bind('<Configure>', _configure_interior)
