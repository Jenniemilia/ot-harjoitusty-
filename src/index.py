from tkinter import Tk
from ui.ui import UI


def main():
    """Construct and run the application"""
    window = Tk()
    window.title("Budjetointisovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
