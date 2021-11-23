from entities.store import Store

class StoreRepository:
    def __init__(self):
        self._stores = [0000]

    def find_all_stores(self):
        return self._stores

    def create_new(self, store):
        stores = self.find_all_stores()
        
        stores.append(store)

        self._stores = stores

        return store

    

store_repository = StoreRepository

