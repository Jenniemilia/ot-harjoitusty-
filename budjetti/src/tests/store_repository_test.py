import unittest
from repositories.store_repository import store_repository
from entities.store import Store

class TestStoreRepository(unittest.TestCase):
    def setUp(self):
        store_repository.delete_all_stores()
        self.store_1234 = Store(1234, "aleksi1234")
        self.store_9876 = Store(9876, "Vantaa9876")

    def test_register_for_one_new_store(self):
        store_repository.create_new(self.store_9876)
        stores = store_repository.find_all_stores()

        self.assertEqual(len(stores), 1)
        self.assertEqual(stores[0].storenumber, self.store_9876.storenumber)

    def test_register_two_new_store(self):
        store_repository.create_new(self.store_9876)
        store_repository.create_new(self.store_1234)

        stores = store_repository.find_all_stores()

        self.assertEqual(len(stores), 2)
        self.assertEqual(stores[0].storenumber, self.store_9876.storenumber)
        self.assertEqual(stores[1].storenumber, self.store_1234.storenumber)

    def test_find_by_storenumber(self):
        store_repository.create_new(self.store_9876)
        store_repository.create_new(self.store_1234)

        store = store_repository.find_by_storenumber(self.store_9876.storenumber)
        self.assertEqual(store.storenumber, self.store_9876.storenumber)




    



