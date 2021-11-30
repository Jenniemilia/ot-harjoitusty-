from entities.budget import Budget
from database_connection import get_database_connection

class BudgetRepository:
    """Luokka joka vastaa budgetin tietokantaan liittyvistä operaatioista"""

    def __init__(self, file_path):
        """Luokan konstruktori
        
        Args:
            file_path: polku tiedostoon johon toteutuneet myynnit tallennetaan."""

        self._file_path = file_path

    def insert_monthly_budget(self, date, budget, store_id):
        """Tallentaa kuluvan tuloskauden myynnit tietokantaan"""

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO sales (month, sales, store_id) VALUES (?,?,?)", (date, budget,store_id))

        self._connection.commit()

    def insert_sales_LY(self, month, budget, store_id):
        """Tallentaa edellisen tuloskauden myynnit tietokantaan"""

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO budget (month, budget, store_id) VALUES (?,?,?)", (month, budget, store_id))

        self._connection.commit()


    
budget_repository = BudgetRepository(get_database_connection())
