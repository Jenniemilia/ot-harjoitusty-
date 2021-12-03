from entities.kpi import Kpi
from database_connection import get_database_connection

class KpiRepository:
    """Luokka joka hoitaa avainlukuihin liittyvän kommunikaation tietokannan kanssa.
    """

    def __init__(self):
        pass


kpi_repository = KpiRepository(get_database_connection())
