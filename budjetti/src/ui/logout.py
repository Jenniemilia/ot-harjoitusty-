from tkinter import ttk, constants

class LogoutView:
    def __init__(self, root):
        self._root = root

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()