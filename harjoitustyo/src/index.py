from tkinter import Tk
from ui.UI import UI

def main():
    window = Tk()
    window.title("Vaalituloslaskuri")
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == '__main__':
    main()
