
from tkinter import Tk
from ui.login import LoginView
from ui.register import RegisterView
from ui.store_view import StoreView
from ui.logout import LogoutView
from ui.admin_view import AdminView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._views = [
            self._show_login_view,
            self._show_register_view,
            self._show_admin_view,
            self._show_store_view,
            self._show_logout_view]

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._views
        )

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._views
        )

        self._current_view.pack()

    def _show_admin_view(self):
        self._hide_current_view()

        self._current_view = AdminView(
            self._root,
            self._views
        )

        self._current_view.pack()

    def _show_store_view(self):
        self._hide_current_view()

        self._current_view = StoreView(
            self._root, 
            self._views
        )

        self._current_view.pack()

    def _show_logout_view(self):
        self._hide_current_view()

        self._current_view = LogoutView(
            self._root
        )

        self._current_view.pack()

