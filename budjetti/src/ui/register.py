from tkinter import ttk, constants
from services.store_service import store_service

class RegisterView:
    def __init__(self, root, views):
        self._root = root
        self._views = views
        self._frame = None
        self._storenumber_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _create_new_store(self):
        storenumber = self._storenumber_entry.get()
        password = self._password_entry.get()
        password_confirmation = self._password_confirmation_entry.get()

        store_service.register(storenumber, password, password_confirmation)
        text=f'Store {storenumber} was registered'
        self._views[3]()

    def _initialize_storenumber_section(self):
        storenumber_label = ttk.Label(master=self._frame, text="Storenumber")
        self._storenumber_entry = ttk.Entry(master=self._frame)

        storenumber_label.grid(padx=5, pady=5, sticky=constants.W)
        self._storenumber_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_section(self):
        password_label = ttk.Label(master=self._frame, text='Password')

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_confirmation_section(self):
        password_confirmation_label = ttk.Label(master=self._frame, text='Confirm Password')

        self._password_confirmation_entry = ttk.Entry(master=self._frame)

        password_confirmation_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_confirmation_entry.grid(padx=5, pady=5, sticky=constants.EW)



    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_storenumber_section()
        self._initialize_password_section()
        self._initialize_password_confirmation_section()

        create_store_button = ttk.Button(master=self._frame, text="Register new store", command=self._create_new_store)

        login_button = ttk.Button(master=self._frame, text="Login", command=self._views[0])

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_store_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)



    