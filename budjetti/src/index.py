from tkinter import Tk
from ui.ui import UI
   
def main():
    window = Tk()
    window.title("Budjettisovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


main()


