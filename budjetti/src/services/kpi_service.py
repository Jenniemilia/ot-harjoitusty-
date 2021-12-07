from entities.kpi import Kpi

from repositories.kpi_repository import kpi_repository


class KpiService:
    """Luokka joka hoitaa avainlukuihin liittyvän laskennan repositoryn kanssa."""

    def __init__(self, kpi_repository):
        pass
        self.kpi_repository = kpi_repository


        

    def find_kpi(self, kpi):
        if kpi in self.key_figures:
            return self.key_figures[kpi]

        return Unknown(self.io)

class Cr:
    def __init__(self, io):
        self.io = io

    def calcultate(self):
        
        get_ly_cr = self._kpi_repository.get_cr(cr)
        

        cr_goal = cr_ly + {self.io}
        pass

class Unknown:
    def __init__(self):
        pass

kpi_service = KpiService(kpi_repository)
