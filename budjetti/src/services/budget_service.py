from entities.budget import Budget

from repositories.budget_repository import budget_repository

class BudgetService:
    def __init__(self, budget_repository):
        self._budget_repository = budget_repository
        self.store = None

    def get_monthly_sales(self):
        """Hakee tietyn kuukauden myynnin"""
        pass

    def get_total_fiscal_year_sales(self, store_id):
        """Hakee koko edellisen tulposkauden myynnin"""

        return self._budget_repository.get_sales_from_total_fiscal_year(store_id)

budget_service = BudgetService(budget_repository)



