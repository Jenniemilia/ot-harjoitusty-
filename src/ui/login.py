
from tkinter import ttk, constants, StringVar
from services.store_service import store_service


class LoginView:
    """Class for login"""

    def __init__(self, root, views):
        """Constructor, initializes class attributes

        Args:
            root: main frame
            views: a list from other views, transition takes place
            according to the index of the list.
        """

        self._root = root
        self._views = views
        self._frame = None
        self._storenumber_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Compress the main frame"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the main frame"""

        self._frame.destroy()

    def _login(self):
        storenumber = self._storenumber_entry.get()
        password = self._password_entry.get()

        store_service.login(storenumber, password)
        self._views[2]()

    def _initialize_storenumber_section(self):
        storenumber_label = ttk.Label(master=self._frame, text="Storenumber")
        self._storenumber_entry = ttk.Entry(master=self._frame)

        storenumber_label.grid(row=2, column=0, padx=5, pady=5)
        self._storenumber_entry.grid(padx=5, pady=5)

    def _initialize_password_section(self):

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(column=0, padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)


    def _initialize(self):
        """Initialize main view"""
        self._frame = ttk.Frame(master=self._root)

        self._initialize_storenumber_section()
        self._initialize_password_section()

        login_button = ttk.Button(master=self._frame, text="Login", command=self._login)

        register_button = ttk.Button(master=self._frame, text="Register", command=self._views[1])

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)


        login_button.grid(padx=5, pady=5)
        text_label = ttk.Label(master=self._frame,
        text="If you don't have account yet, register here")
        text_label.grid(column=0, padx=5, pady=5)
        register_button.grid(padx=5, pady=5)



