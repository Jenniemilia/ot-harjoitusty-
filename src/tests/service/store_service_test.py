import unittest
from entities.budget import Budget
from entities.store import Store
from services.budget_service import BudgetService
from services.store_service import (
    StoreService,
    InvalidCredentialsError,
    UserInputError,
    UsernameExistsError)

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

    def create_new(self, storenumber):
        self.stores.append(storenumber)

        return storenumber

    def delete_all(self):
        self.stores = []

class TestStoreService(unittest.TestCase):
    def setUp(self):
        self.store_service = StoreService(
            FakeStoreRepository()
        )
    
        self.store_1234 = Store(1234, 'myymala1')
    
    def login(self, store):
        self.store_service.register(store.storenumber, store.password, store.password)

    def test_login_with_valid_storenumber_and_password(self):

        self.store_service.register(self.store_1234.storenumber, self.store_1234.password, self.store_1234.password)

        store = self.store_service.login(self.store_1234.storenumber, self.store_1234.password)
        self.assertEqual(store.storenumber, self.store_1234.storenumber)

    def test_login_with_invalid_storenumber(self):
        
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.store_service.login('3344', 'myymala1')
        )

    def test_login_with_invalid_password(self):

        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.store_service.login('1234', 'salasana3')
        )        

    def test_get_current_store(self):
        self.login(self.store_1234)

        current_store = self.store_service.get_current_store()

        self.assertEqual(current_store.storenumber, self.store_1234.storenumber)

    def test_register_with_too_short_password(self):
        
        self.assertRaises(
            UserInputError,
            lambda: self.store_service.register('1234', 'sala1', 'sala1')
        )        

    def test_to_register_with_existing_store_number(self):

        self.store_service.register(self.store_1234.storenumber, self.store_1234.password, self.store_1234.password)

        self.assertRaises(
            UsernameExistsError,
            lambda: self.store_service.register(self.store_1234.storenumber, 'salasana1', 'salasana1')
        )       