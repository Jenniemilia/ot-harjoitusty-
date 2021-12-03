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

    def _CR_kpi_handler(self):
        cr = self._month_CR_entry.get()

        kpi_service.calculate(cr)


    def _initialize_header(self):
        header_label = ttk.Label(master=self._frame,
        text=f"You are logged in with storenumber: {self._store.storenumber}")

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize_store_budget(self):
        monthly_budget_label = ttk.Label(master=self._store_budget_frame,
        text=f"Your monthly budget for November is 145000")
        
        ly_sales_label = ttk.Label(master=self._frame,
        text=f"Sales from LY November 139000")


        monthly_budget_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        ly_sales_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

    def _initialize_kpi_calculator(self):
        monthly_kpi_targets_label = ttk.Label(master=self._store_kpi_frame,
        text= "Aseta avainlukutavoitteet")

        month_CR_label = ttk.Label(master=monthly_kpi_targets_label,
        text="CR tavoite:")
        self._month_CR_entry = ttk.Entry(master=self._store_kpi_frame)


    def _initialize_footer(self):
        pass




    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._store_budget_frame = ttk.Frame(master=self._frame)
        self._store_kpi_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_store_budget()
        self._initialize_kpi_calculator()
        self._initialize_footer()

        self._store_budget_frame.grid(row=2, column=1)

        self._frame.grid_columnconfigure(0, weight=1)









