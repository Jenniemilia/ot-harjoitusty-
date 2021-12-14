from tkinter import Button, ttk, StringVar, constants
from services.store_service import store_service
from services.budget_service import BudgetService, budget_service

class AdminView:
    """Class that contains all the information of previous fiscal year budget and has
    the tools to adjust the budget
    """

    def __init__(self, root, views):
        self._root = root
        self._views = views
        self._label_var = None
        self._frame = None
        self._store = store_service.get_current_store()
        self._storenumber = store_service.get_storenumber_by_id(self._store)
        self._ly_total_sales = budget_service.get_total_fiscal_year_sales(self._store)

        self.initialize()

    def pack(self):
        """Compresses the main frame"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the main frame"""

        self._frame.destroy()

    def _logout_handler(self):
        store_service.logout()
        self._views[0]

    def convert_target(self):
        """Convert LY sales based on growth plan"""

        growth_plan = self._budget_entry.get()
        growth_plan = int(growth_plan)

        self.calculator = ((self._ly_total_sales) * (growth_plan + 100))/100
        budget_service.edit_yearly_target_budget(self.calculator, self._store)

        budget_outcome_label = ttk.Label(master=self._frame,
        text=f"Budget for the fiscal year 2021-2022: {self.calculator}")
        budget_outcome_label.grid(row=5, padx=5, pady=5, sticky=(constants.E, constants.W))


    def convert_personal_costs(self):
        """Calculate the personal costs budget in accordance with the budget
        for the following financial year"""

        personal_costs_budget = self._personal_cost_entry.get()
        personal_costs_budget = int(personal_costs_budget )

        self.pc_calculator = (self.calculator * (personal_costs_budget))/100

        personal_cost_label = ttk.Label(master=self._frame,
        text=f"Personal cost budget for the fiscal year 2021-2022: {self.pc_calculator}")
        personal_cost_label.grid(row=9, padx=5, pady=5, sticky=(constants.E, constants.W))


    def _initialize_header(self):

        store_label = ttk.Label(master=self._frame,
        text=f"Welcome to store {self._storenumber}")

        store_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))

        ly_sales_info_label = ttk.Label(master=self._frame,
        text=f"Last Fiscal Year sales total: {self._ly_total_sales}")

        ly_sales_info_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))


    def _initialize_budget_calculator(self):

        budget_label = ttk.Label(master=self._frame, text=f"Add the growth target as a percentage")
        self._budget_entry = ttk.Entry(master=self._frame)

        budget_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))
        self._budget_entry.grid(row=4, column=0, padx=5, pady=5)

        """Convert button"""
        budget_button = ttk.Button(master=self._frame, text="Confirm",
        command=self.convert_target)
        budget_button.grid(row=4, column=1, padx=5, pady=5,
        sticky=(constants.E, constants.W))

    def _initialize_personal_cost_calculator(self):

        personal_cost_label = ttk.Label(master=self._frame,
        text="Add the percentage for personal costs budget")
        self._personal_cost_entry = ttk.Entry(master=self._frame)

        personal_cost_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5,
        sticky=(constants.E, constants.W))
        self._personal_cost_entry.grid(row=8, column=0, padx=5, pady=5)

        """Convert button"""
        personal_cost_button = ttk.Button(master=self._frame, text="Confirm",
        command=self.convert_personal_costs)
        personal_cost_button.grid(row=8, column=1, padx=5, pady=5,
        sticky=(constants.E, constants.W))

    def _initialize_footer(self):
        footer_label = ttk.Label(master=self._frame,
        text="Go to calculate the key performance indicators")

        footer_label.grid(row=11, padx=5, pady=5, sticky=(constants.E, constants.W))

        footer_button = ttk.Button(master=self._frame, text="Move to KPI", command=self._views[3])
        footer_button.grid(row=12, padx=5, pady=5)

        log_out_button = ttk.Button(master=self._frame, text="Log out", command=self._logout_handler)
        log_out_button.grid(row=13, padx=12, pady=5)


    def initialize(self):
        """Initialize main view"""
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_budget_calculator()
        self._initialize_personal_cost_calculator()
        self._initialize_footer()



