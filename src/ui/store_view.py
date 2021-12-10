from tkinter import ttk, constants
import datetime as dt
from services.store_service import store_service
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
        pass


    def _initialize_header(self):

        date = dt.datetime.now()
        header_date = ttk.Label(master=self._frame, text=f"{date:%A, %d.%m.%Y}", font="Calibri, 12")

        header_date.grid(row=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))

        header_label = ttk.Label(master=self._frame,
        text=f"Welcome! You are logged in with storenumber: {self._store.storenumber}", font="Calibri, 12")

        header_label.grid(row=1, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))



    def _initialize_store_budget(self):
        yearly_budget_label = ttk.Label(master=self._frame, 
        text=f"This fiscal year budget this comes from database")

        monthly_budget_label = ttk.Label(master=self._frame,
        text=f"Your monthly budget for November is 145000")

        ly_sales_label = ttk.Label(master=self._frame,
        text=f"Sales from LY November {self._monthly_budget}")

        yearly_budget_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        monthly_budget_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)
        ly_sales_label.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)

    def _initialize_kpi_calculator(self):
        monthly_kpi_targets_label = ttk.Label(master=self._frame,
        text= "Calculate Key Figure targets")

        month_CR_label = ttk.Label(master=self._frame,
        text="CR tavoite:")
        month_CR_entry = ttk.Entry(master=self._frame)
        cr_button = ttk.Button(master=self._frame,
        text="Confirm", command=self._CR_kpi_handler)

        monthly_kpi_targets_label.grid()
        month_CR_label.grid(row=7,column=0, padx=5, pady=5, sticky=constants.W)
        month_CR_entry.grid(row=8,column=0, padx=5, pady=5)

        cr_button.grid(row=8, column=1, padx=5, pady=5)

    def _initialize_footer(self):
        pass




    def _initialize(self):
        """Initialize page view"""

        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_store_budget()
        self._initialize_kpi_calculator()
        self._initialize_footer()










