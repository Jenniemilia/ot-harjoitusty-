from tkinter import ttk, constants
from services.store_service import store_service
from services.kpi_service import kpi_service
from services.budget_service import budget_service

class StoreView:
    def __init__(self, root, views):
        self._root = root
        self._views = views
        self._frame = None
        self._store = store_service.get_current_store()
        self._monthly_budget = budget_service.get_total_fiscal_year_sales(self._store.storenumber)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _CR_kpi_handler(self):
        cr = self._month_CR_entry.get()

        kpi_service.find_kpi(cr)


    def _initialize_header(self):
        header_label = ttk.Label(master=self._frame,
        text=f"You are logged in with storenumber: {self._store.storenumber}")

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))

    def _initialize_store_budget(self):
        monthly_budget_label = ttk.Label(master=self._root,
        text=f"Your monthly budget for November is 145000")

        ly_sales_label = ttk.Label(master=self._root,
        text=f"Sales from LY November {self._monthly_budget}")


        monthly_budget_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        ly_sales_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

    def _initialize_kpi_calculator(self):
        monthly_kpi_targets_label = ttk.Label(master=self._root,
        text= "Aseta avainlukutavoitteet")

        month_CR_label = ttk.Label(master=monthly_kpi_targets_label,
        text="CR tavoite:")
        self._month_CR_entry = ttk.Entry(master=self._frame)
        cr_button = ttk.Button(monthly_kpi_targets_label,
        text="Confirm", command=self._CR_kpi_handler)

        month_CR_label.grid(row=4,column=0, padx=5, pady=5, sticky=constants.W)
        cr_button.grid(column=1, padx=5, pady=5)

    def _initialize_footer(self):
        pass




    def _initialize(self):
        """Alustaa näkymän"""

        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_store_budget()
        self._initialize_kpi_calculator()
        self._initialize_footer()

        self._frame.grid_columnconfigure(0, weight=1)









