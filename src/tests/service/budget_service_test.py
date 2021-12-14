import unittest
from entities.budget import Budget
from entities.store import Store
from services.budget_service import BudgetService
from services.store_service import (
    StoreService,
    InvalidCredentialsError)

class FakeBudgetRepository:
    def __init__(self, sales = None):
        self.sales = sales or []

    def get_total_sales_last_fiscal(self):
        return self.get_total_sales

class FakeStoreRepository:
    def __init__(self, stores=None):
        self.stores= stores or []

    def find_all(self):
        return self.stores

    def find_by_storenumber(self, storenumber):
        matching_stores = filter(
            lambda store: store.storenumber == storenumber,
            self.stores
        )

        matching_stores_list = list(matching_stores)
        return matching_stores_list[0] if len(matching_stores_list) > 0 else None

    def create_new_store(self, storenumber):
        self.stores.append(storenumber)

        return storenumber

    def delete_all(self):
        self.stores = []

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.store_service = StoreService(
            FakeBudgetRepository(),
            FakeStoreRepository()
        )
    
        self.store_1234 = Store('1234', 'myymala1')

    def test_login_with_valid_storenumber_and_password(self):
        self.store_service.register(self.store_1234.storenumber, self.store_1234.password)

        store = self.store_service.login(self.store_1234.storenumber, self.store_1234.password)

        self.assertEqual(store.storenumber, self.store_1234.storenumber)


    