from entities.budget import Budget
from database_connection import get_database_connection

def get_sales_by_month(row):
    return Budget(row["month"], row["sales_ly"], row["traffic"]) if row else None

class BudgetRepository:
    """The category responsible for budget database operations"""

    def __init__(self, connection):
        """Class constructor

        Args:
            file_path: the path to the file where the actual sales are saved."""

        self._connection = connection

    def get_sales_by_month(self, month, store_id):
        """Retrieves the sales for the previous fiscal year on a monthly basis"""

        cursor = self._connection.cursor()

        cursor.execute("SELECT sales_ly FROM Ly_fiscal WHERE month = ? AND store_id = ?",
        [month, store_id])

        result = cursor.fetchone()

        return result[0]

    def get_traffic_by_month(self, month, store_id):
        "Retrieves teh traffic for the previous fiscal year on a monthly basis"

        cursor =  self._connection.cursor()

        cursor.execute("SELECT traffic FROM Ly_fiscal WHERE month = ? AND store_id = ?",
        [month, store_id])

        result = cursor.fetchone()
        return result[0]

    def get_sales_from_total_fiscal_year(self, store_id):
        """Retrieves the actual sales for the entire previous fiscal year"""

        cursor = self._connection.cursor()

        cursor.execute("SELECT SUM(sales_ly) FROM Ly_fiscal WHERE store_id = ?", [store_id])

        result = cursor.fetchone()
        return result[0]


    def check_if_values_budget(self, store_id):
        """Checks if earlier values in the table"""

        cursor = self._connection.cursor()

        cursor.execute("SELECT count(*) FROM Yearly_targets targets WHERE store_id = ?", [store_id])

        result = cursor.fetchone()
        if result[0] == 0:
            return False

        return True

    def insert_yearly_target_budget(self, new_budget, store_id):
        """Insert yearly targets to database"""

        cursor = self._connection.cursor()

        cursor.execute("""INSERT INTO Yearly_targets (budget, store_id) values (?, ?)""",
        [new_budget, store_id])

        self._connection.commit()

    def edit_yearly_target_budget(self, new_budget, store_id):
        """Edit yearly targets given by user"""

        cursor = self._connection.cursor()

        cursor.execute("UPDATE Yearly_targets SET budget = ? WHERE store_id = ?",
        [new_budget, store_id])

        self._connection.commit()

    def get_new_budget(self, store_id):

        cursor = self._connection.cursor()

        cursor.execute("SELECT budget FROM Yearly_targets WHERE store_id = ?", [store_id])

        result = cursor.fetchone()
        return result[0]

    def get_yearly_kpi_figures_by_month(self, store_id, month):

        cursor = self._connection.cursor()

        cursor.execute("""SELECT cr, ipt, apt FROM Ly_kpi WHERE store_id = ? AND month = ?""",
        [store_id, month])

        result = cursor.fetchone()
        return result

budget_repository = BudgetRepository(get_database_connection())


