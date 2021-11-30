from tkinter import ttk, constants
from services.store_service import store_service

class StoreView:
    def __init__(self, root, views):
        self._root = root
        self.views = views
        self._frame = None
        self._store = store_service.get_current_store()
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header_label = ttk.Label(master=self._frame, 
        text=f"You are logged in with storenumber: {self._store.storenumber}")

        header_label.grid(padx=5, pady=5, sticky=constants.W)

    def _initialize_store_budget(self):
        monthly_budget_label = ttk.Label(master=self._frame,
        text=f"Your monthly budget for November is 145000")
        monthly_budget_label.grid(padx=5, pady=5, sticky=constants.W)

        




    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_store_budget()



    

