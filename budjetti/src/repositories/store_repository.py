from entities.store import Store
from database_connection import get_database_connection

def get_store_by_row(row):
    return Store(row["storenumber"], row["password"]) if row else None

class StoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_stores(self):
        cursor = self._connection.cursor()

        cursor.execute('select * from stores')

        rows = cursor.fetchall()

        return list(map(get_store_by_row, rows))

    def find_by_storenumber(self, storenumber):

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM stores WHERE storenumber = ?", (storenumber,))

        row = cursor.fetchone()

        return get_store_by_row(row)

    def create_new(self, store):
        """Tallentaa uuden myymälän tietokantaan"""

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO stores (storenumber, password) VALUES (?,?)", (store.storenumber, store.password))

        self._connection.commit()

        return store

    def delete_all_stores(self):

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM stores")

        self._connection.commit()

    

store_repository = StoreRepository(get_database_connection())

