from entities.kpi import Kpi
from database_connection import get_database_connection

class KpiRepository:
    """Class that handles key figure related communication with the database
    """

    def __init__(self, connection):
        self.connection = connection


kpi_repository = KpiRepository(get_database_connection())
