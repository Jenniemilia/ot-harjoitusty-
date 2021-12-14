from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database


def main():
    """Construct and run the application"""
    initialize_database()
    window = Tk()
    window.title("Budjetointisovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
