from entities.budget import Budget
from database_connection import get_database_connection

def get_sales_by_month(row):
    return Budget(row["month"], row["sales"], row["tarffic"]) if row else None

class BudgetRepository:
    """Luokka joka vastaa budgetin tietokantaan liittyvistä operaatioista"""

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            file_path: polku tiedostoon johon toteutuneet myynnit tallennetaan."""

        self._connection = connection

    def get_sales_by_month(self, month, store_id):
        """Hakee edellisen tuloskauden myynnin kuukausitasolla"""

        cursor = self._connection.cursor()

        cursor.execute("SELECT month, sales_ly FROM budget WHERE month = ? AND store_id = ?",
        [month, store_id])

        row = cursor.fetchone()

        return get_sales_by_month(row)

    def get_sales_from_total_fiscal_year(self, store_id):
        """Hakee koko edellisen tuloskauden toteutuneen myynnin"""

        cursor = self._connection.cursor()
 
        cursor.execute("SELECT SUM(sales_ly) FROM budget WHERE store_id= ?", [store_id])

        result = cursor.fetchone()
        result = result[0]

        return result


budget_repository = BudgetRepository(get_database_connection())
