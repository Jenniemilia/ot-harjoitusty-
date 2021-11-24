
from tkinter import Tk
from ui.login import LoginView
from ui.register import RegisterView

class UI:
    def __init__(self, root):
        self._root = root
        self._current = None

    def start(self):
        self._show_login()

    def _hide_current(self):
        if self._current:
            self._current.destroy()

        self._current = None

    def _handle_login(self):
        self._show_login()

    def _handle_register(self):
        self._show_register()

    def _show_login(self):
        self._hide_current()

        self._current = LoginView(
            self._root,
            self._show_register,
            self._handle_register
        )

        self._current.pack()


    def _show_register(self):
        self._hide_current()

        self._current = RegisterView(
            self._root,
            self._show_login,
            self._handle_login
        )

        self._current.pack()
