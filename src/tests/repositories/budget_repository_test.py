import unittest, sqlite3

from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.budget_repository import budget_repository
from repositories.store_repository import store_repository
from entities.budget import Budget
from entities.store import Store

class TestStoreRepository(unittest.TestCase):
    def setUp(self):

        self.test_db = get_database_connection()
        initialize_database()

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

    def test_if_earlier_values_in_target_table(self):
        target = budget_repository.check_if_values_budget(1)
        self.assertEqual(target, False)

    def test_insert_yearly_target_and_check_table(self):
        budget_repository.insert_yearly_target_budget(100000, 1)
        target = budget_repository.check_if_values_budget(1)
        self.assertEqual(target, True)

    def test_insert_yearly_target_and_get_right_value(self):
        new_target = 100000
        budget_repository.insert_yearly_target_budget(new_target, 1)
        get_target = budget_repository.get_new_budget(1)
        self.assertEqual(get_target, new_target)

    def test_edit_yearly_target_budget(self):
        budget_repository.insert_yearly_target_budget(100000, 1)
        budget_repository.edit_yearly_target_budget(200000, 1)
        get_target = budget_repository.get_new_budget(1)
        self.assertEqual(get_target, 200000)

    def test_check_if_kpi_values_in_database(self):
        store_1 = budget_repository.check_if_kpi(1)
        self.assertEqual(store_1, True)

        store_2 = budget_repository.check_if_kpi(2)
        self.assertEqual(store_2, False)

   

        

    

    
