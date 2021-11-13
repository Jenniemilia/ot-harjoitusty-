from tkinter import ttk

class UI:
    def __init__(self, root):
        self._root = root
        self._current_viwe = None

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        heading_label.pack()
        username_label.pack()
        username_entry.pack()