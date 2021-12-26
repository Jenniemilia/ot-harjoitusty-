import unittest

from repositories.budget_repository import budget_repository
from repositories.store_repository import store_repository
from entities.budget import Budget
from entities.store import Store

class TestStoreRepository(unittest.TestCase):
    def setUp(self):

        store_repository.delete_all_stores()
        
        self.store_1234 = Store(1234, "aleksi1234")
        self.sales_december = Budget(12, 147000, 17950, 1)

    def test_get_sales_by_month(self):
        sales = budget_repository.get_sales_by_month(12,1)
        self.assertEqual(sales, self.sales_december.sales_ly)

    def test_get_traffic_by_month(self):
        traffic = budget_repository.get_traffic_by_month(12,1)
        self.assertEqual(traffic, self.sales_december.traffic)

    def test_get_sales_from_total_fiscal(self):
        total_sales = budget_repository.get_sales_from_total_fiscal_year(1)
        self.assertEqual(total_sales, 1678820)

    def test_get_kpi_from_last_year_december(self):
        kpi_december = budget_repository.get_yearly_kpi_figures_by_month(1,12)
        self.assertEqual(kpi_december[0], 16.3)

   

        

    

    
