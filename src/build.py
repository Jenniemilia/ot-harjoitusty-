"""Initialize everything ready for the application"""

from initialize_database import initialize_database

"""Initializes database"""
def build():
    initialize_database()

if __name__ == "__main__":
    build()
