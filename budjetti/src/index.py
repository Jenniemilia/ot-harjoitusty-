from tkinter import Tk
import customtkinter
from ui.ui import UI
from initialize_database import initialize_database


def main():
    window = Tk()
    window.geometry("500x500")
    window.title("Budjettisovellus")

    initialize_database()

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()


