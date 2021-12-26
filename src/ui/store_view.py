from tkinter import ttk, constants
from datetime import date
from services.store_service import store_service
from services.budget_service import budget_service

class StoreView:
    """Class that contains all the functionality in the store view"""
    def __init__(self, root, views):
        self._root = root
        self._views = views
        self._frame = None
        self._store = store_service.get_current_store()
        self._store_id = store_service.get_store_id_by_storenumber(self._store.storenumber)

        self._initialize()

    def pack(self):
        """Compresses the main frame"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the main frame"""
        self._frame.destroy()

    def _logout_handler(self):
        store_service.logout()
        self._views[0]()

    def _CR_kpi_handler(self):
        cr_plan = self._month_CR_entry.get()
        cr_plan = float(cr_plan)

        self.kpi_calculator = (self._kpi_figures[0] + cr_plan)

        cr_plan_outcome_label = ttk.Label(master=self._frame,
        text=f"CR target: {self.kpi_calculator:.2f}")
        cr_plan_outcome_label.grid(row=15, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _IPT_kpi_handler(self):
        ipt_plan = self._month_IPT_entry.get()
        ipt_plan = float(ipt_plan)

        self.ipt_calculator = (self._kpi_figures[1] *(ipt_plan/100+1))

        ipt_plan_outcome_label = ttk.Label(master=self._frame,
        text=f"IPT target: {self.ipt_calculator:.2f}")
        ipt_plan_outcome_label.grid(row=17, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _AUR_kpi_handler(self):
        aur_plan = self._month_AUR_entry.get()
        aur_plan = float(aur_plan)

        self.aur_calculator = (self._ly_aur_calculator * (aur_plan/100+1))
        self.apt_calculator = (self.aur_calculator * self.ipt_calculator)

        aur_plan_outcome_label = ttk.Label(master=self._frame,
        text=f"AUR target: {self.aur_calculator:.2f}")
        aur_plan_outcome_label.grid(row=19, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        
        apt_plan_outcome_label = ttk.Label(master=self._frame,
        text=f"APT target: {self.apt_calculator:.2f}")
        apt_plan_outcome_label.grid(row=20, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _traffic_handler(self):
        traffic_plan = self._month_traffic_entry.get()
        traffic_plan = float(traffic_plan)

        self.traffic_calculator = int(self._ly_traffic * (traffic_plan/100+1))

        traffic_plan_outcome_label = ttk.Label(master=self._frame,
        text=f"Traffic target: {self.traffic_calculator}")
        traffic_plan_outcome_label.grid(row=22, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _total_month_handler(self):
        self._total_month_calculator = ((self.kpi_calculator/100) * self.ipt_calculator *
        self.aur_calculator * self.traffic_calculator)

        total_month_result_label = ttk.Label(master=self._frame,
        text=f"Netsale for this month would be {self._total_month_calculator:.2f}€")
        total_month_result_label.grid(row=24, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))

    def _initialize_header(self):

        self.date = date.today()
        header_date = ttk.Label(master=self._frame,
        text=f"Welcome! {self.date}", font="Calibri, 12")

        header_date.grid(row=0, columnspan=2, padx=10, pady=10,
        sticky=(constants.E, constants.W))

        header_label = ttk.Label(master=self._frame,
        text=f"You are logged in with storenumber: {self._store.storenumber}", font="Calibri, 12")

        header_label.grid(row=1, columnspan=2, padx=10, pady=10,
        sticky=(constants.E, constants.W))

    def _initialize_store_budget(self):

        self._monthly_budget = budget_service.get_last_year_sales_by_month(self._store_id)
        self._new_budget = budget_service.get_new_budget_for_current_fiscal(self._store_id)

        yearly_budget_label = ttk.Label(master=self._frame, 
        text=f"This fiscal year budget: {self._new_budget} €")

        self._month_budget_calculator = round(self._new_budget/12, 2)
        monthly_budget_label = ttk.Label(master=self._frame,
        text=f"Your monthly budget for {self.date.month}.{self.date.year}: {self._month_budget_calculator} €")

        last_year = (self.date.year) -1
        ly_sales_label = ttk.Label(master=self._frame,
        text=f"Sales from LY {self.date.month}.{last_year}: {self._monthly_budget} €")

        self._variation_calculator = ((self._month_budget_calculator/self._monthly_budget-1)*100)
        variation_label = ttk.Label(master=self._frame, text=f"Variation: {self._variation_calculator:.2f}%", foreground="green")

        yearly_budget_label.grid(row=3, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        monthly_budget_label.grid(row=4, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        ly_sales_label.grid(row=5, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        variation_label.grid(row=6, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize_ly_kpi_values(self):

        self._kpi_figures = budget_service.get_yearly_kpi_figures_by_month(self._store_id)
        self._ly_traffic = budget_service.get_last_year_traffic_by_month(self._store_id)

        ly_kpi_values_header = ttk.Label(master=self._frame,
        text=f"KPI's from last fiscal year")

        ly_kpi_values_header.grid(row=7, column=0, padx=5, pady=5, sticky=constants.W)
        self._ly_aur_calculator = (self._kpi_figures[2] / self._kpi_figures[1])

        ly_CR_header = ttk.Label(master=self._frame, text=f"CR:      {self._kpi_figures[0]} %")
        ly_IPT_header = ttk.Label(master=self._frame, text=f"IPT:    {self._kpi_figures[1]} KPL")
        ly_APT_header = ttk.Label(master=self._frame, text=f"APT:    {self._kpi_figures[2]} €")
        ly_AUR_header = ttk.Label(master=self._frame, text=f"AUR:    {self._ly_aur_calculator:.2f} €")
        ly_traffic_header = ttk.Label(master=self._frame, text=f"Traffic:   {self._ly_traffic}")

        ly_CR_header.grid(row=8, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        ly_IPT_header.grid(row=9, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        ly_APT_header.grid(row=10, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        ly_AUR_header.grid(row=11, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        ly_traffic_header.grid(row=12, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize_kpi_calculator(self):
        monthly_kpi_targets_label = ttk.Label(master=self._frame,
        text= """Calculate Key Figure targets for this month:""")

        month_CR_label = ttk.Label(master=self._frame,
        text="CR growth in %:")
        self._month_CR_entry = ttk.Entry(master=self._frame)
        cr_button = ttk.Button(master=self._frame,
        text="Confirm", command=self._CR_kpi_handler)

        monthly_kpi_targets_label.grid(row=13, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        month_CR_label.grid(row=14, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        self._month_CR_entry.grid(row=14, column=1, padx=3, pady=3)

        cr_button.grid(row=14, column=2, padx=3, pady=3)

        month_IPT_label = ttk.Label(master=self._frame,
        text="Calculate IPT growth in %:")
        self._month_IPT_entry = ttk.Entry(master=self._frame)
        ipt_button = ttk.Button(master=self._frame, text="Confirm", command=self._IPT_kpi_handler)

        month_IPT_label.grid(row=16, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        self._month_IPT_entry.grid(row=16, column=1, padx=3, pady=3)
        ipt_button.grid(row=16, column=2, padx=3, pady=3)

        month_AUR_label = ttk.Label(master=self._frame, 
        text="Calculate AUR growth in %:")
        self._month_AUR_entry = ttk.Entry(master=self._frame)
        aur_button = ttk.Button(master=self._frame, text="Confirm", command=self._AUR_kpi_handler)

        month_AUR_label.grid(row=18, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        self._month_AUR_entry.grid(row=18, column=1, padx=3, pady=3)
        aur_button.grid(row=18, column=2, padx=3, pady=3)

        month_traffic_label = ttk.Label(master=self._frame,
        text="Calculate traffic growth in %:")
        self._month_traffic_entry = ttk.Entry(master=self._frame)
        traffic_button= ttk.Button(master=self._frame, text="Confirm", command=self._traffic_handler)

        month_traffic_label.grid(row=21, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        self._month_traffic_entry.grid(row=21, column=1, padx=3, pady=3)
        traffic_button.grid(row=21, column=2, padx=3, pady=3)

    def _initialize_total_month_budget(self):
        total_month_label = ttk.Label(master=self._frame,
        text="After added kpi growth plans, calculate net sales:")
        total_month_button= ttk.Button(master=self._frame, text="Confirm", command=self._total_month_handler)

        total_month_label.grid(row=23, column=0, padx=3, pady=3, sticky=(constants.E, constants.W))
        total_month_button.grid(row=23, column=1, padx=3, pady=3)



    def _initialize_footer(self):
        go_back_button = ttk.Button(master=self._frame, text="Go back", command=self._views[2])
        go_back_button.grid(row=26, column=1, padx=5, pady=5, sticky=constants.SE)
        log_out_button = ttk.Button(master=self._frame, text="Log out", command=self._logout_handler)
        log_out_button.grid(row=27, column=1, padx=5, pady=5, sticky=constants.SE)

    def _initialize(self):
        """Initialize page view"""

        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_store_budget()
        self._initialize_ly_kpi_values()
        self._initialize_kpi_calculator()
        self._initialize_total_month_budget()
        self._initialize_footer()










