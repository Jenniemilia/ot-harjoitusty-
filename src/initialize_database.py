from database_connection import get_database_connection

def drop_tables(connection):
    """Drops tables if existing"""

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Stores;")
    cursor.execute("DROP TABLE IF EXISTS Ly_fiscal;")
    cursor.execute("DROP TABLE IF EXISTS Ly_kpi;")
    cursor.execute("DROP TABLE IF EXISTS Yearly_targets")

def create_tables(connection):
    """Creates new tables for the database"""

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Stores (id INTEGER PRIMARY KEY,
    storenumber INTEGER, password TEXT)""")

    cursor.execute("""CREATE TABLE Ly_fiscal (id INTEGER PRIMARY KEY, month INTEGER,
    sales_ly INTEGER, traffic INTEGER, store_id REFERENCES stores)""")

    cursor.execute("""CREATE TABLE Ly_kpi (id INTEGER PRIMARY KEY, month INTEGER, cr REAL, ipt REAL,
    apt REAL, store_id REFERENCES stores)""")

    cursor.execute("""CREATE TABLE Yearly_targets (id INTEGER PRIMARY KEY, budget INTEGER,
    personal_costs INTEGER, store_id REFERENCES stores)""")


    connection.commit()


def insert_sales_ly(connection):
    """Add last year figures to the database"""
    cursor= connection.cursor()

    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (1, 148000, 12050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (2, 134000, 11050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (3, 135000, 13050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (4, 142000, 12950, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (5, 145000, 15050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (6, 151000, 18050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (7, 134900, 17150, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (8, 148120, 16850, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (9, 131000, 14350, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (10, 127800, 14050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (11, 135000, 16050, 1)""")
    cursor.execute("""INSERT INTO Ly_fiscal (month, sales_ly, traffic, store_id) values
    (12, 147000, 17950, 1)""")

    connection.commit()

def insert_kpi_ly(connection):
    """Add last year key peformance indicators to database"""

    cursor= connection.cursor()

    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (1, 18, 1.5, 56, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (2, 17.5, 1.2, 45, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (3, 16, 1.4, 46.2, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (4, 16.3, 1.6, 44.8, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (5, 18, 1.5, 56, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (6, 17.5, 1.2, 45, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (7, 16, 1.4, 46.2, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (8, 16.3, 1.6, 44.8, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (9, 17.5, 1.2, 45, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (10, 16, 1.4, 46.2, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (11, 16.3, 1.6, 44.8, 1)""")
    cursor.execute("""INSERT INTO Ly_kpi (month, cr, ipt, apt, store_id) values
    (12, 16.3, 1.6, 44.8, 1)""")

    connection.commit()

def initialize_database():
    """Drops and recreates the tables in the main database"""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_sales_ly(connection)
    insert_kpi_ly(connection)

if __name__ == "__main__":
    initialize_database()
