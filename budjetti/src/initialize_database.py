from sqlite3.dbapi2 import connect
from database_connection import get_database_connection




def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE stores (id INTEGER PRIMARY KEY, 
    storenumber INTEGER, password TEXT);""")

    cursor.execute("""CREATE TABLE budget (id INTEGER PRIMARY KEY, month INTEGER,
    budget INTEGER, store_id REFERENCES stores)""")

    cursor.execute("""CREATE TABLE sales (id INTEGER PRIMARY KEY, month INTEGER,
    sales INTEGER, store_id REFERENCES stores)""")




    connection.commit()

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS stores;")
    cursor.execute("DROP TABLE IF EXISTS budget;")
    cursor.execute("DROP TABLE IF EXISTS sales;")


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
