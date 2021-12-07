from sqlite3.dbapi2 import Cursor, connect
from database_connection import get_database_connection


def drop_tables(connection):
    """Drops tables if existing"""

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS stores;")
    cursor.execute("DROP TABLE IF EXISTS budget;")
    cursor.execute("DROP TABLE IF EXISTS sales;")
    cursor.execute("DROP TABLE IF EXISTS kpi")

def create_tables(connection):
    """Creates new tables for the database"""

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE stores (id INTEGER PRIMARY KEY,
    storenumber INTEGER, password TEXT);""")

    cursor.execute("""CREATE TABLE sales (id INTEGER PRIMARY KEY, month INTEGER,
    sales INTEGER, store_id REFERENCES stores)""")

    cursor.execute("""CREATE TABLE budget (id INTEGER PRIMARY KEY, month INTEGER,
    sales_ly INTEGER, traffic INTEGER, store_id REFERENCES stores)""")

    cursor.execute("""CREATE TABLE kpi (id INTEGER PRIMARY KEY, month INTEGER, cr REAL, ipt REAL,
    apt REAL, store_id REFERENCES stores)""")

    connection.commit()


def insert_sales_ly(connection):
    """Add last year figures to the database"""
    cursor= connection.cursor()

    cursor.execute("""INSERT INTO budget (month, sales_ly, traffic, store_id) values
    (1, 145000, 15050, 1);""")
    cursor.execute("""INSERT INTO budget (month, sales_ly, traffic, store_id) values
    (2, 104000, 10050, 1);""")
    cursor.execute("""INSERT INTO budget (month, sales_ly, traffic, store_id) values
    (3, 125000, 13050, 1);""")
    cursor.execute("""INSERT INTO budget (month, sales_ly, traffic, store_id) values
    (4, 138000, 14950, 1);""")

    connection.commit()

def insert_kpi_ly(connection):
    """Add last year key peformance indicators to database"""

    cursor= connection.cursor()

    cursor.execute("""INSERT INTO kpi (month, cr, ipt, apt, store_id) values
    (1, 18, 1.5, 56, 1);""")
    cursor.execute("""INSERT INTO kpi (month, cr, ipt, apt, store_id) values
    (2, 17.5, 1.2, 45, 1);""")
    cursor.execute("""INSERT INTO kpi (month, cr, ipt, apt, store_id) values
    (3, 16, 1.4, 46.2, 1);""")
    cursor.execute("""INSERT INTO kpi (month, cr, ipt, apt, store_id) values
    (4, 16.3, 1.6, 44.8, 1);""")

    connection.commit()




def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_sales_ly(connection)
    insert_kpi_ly(connection)

if __name__ == "__main__":
    initialize_database()
