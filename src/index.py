from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database


def main():
    initialize_database()
    window = Tk()
    window.geometry("500x500")
    window.title("Budjetointisovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
