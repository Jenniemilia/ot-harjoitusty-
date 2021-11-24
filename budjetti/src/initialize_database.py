from sqlite3.dbapi2 import connect
from database_connection import get_database_connection



def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""create table stores (id INTEGER PRIMARY KEY, 
    storenumber INTEGER, password TEXT);""")

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
