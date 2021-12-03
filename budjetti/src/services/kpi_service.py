from entities.kpi import Kpi

from repositories.kpi_repository import kpi_repository


class KpiService:
    """Luokka joka hoitaa avainlukuihin liittyvän laskennan repositoryn kanssa."""

    def __init__(self, kpi_repository):
        self.kpi_repository = kpi_repository

        self.key_figures = {
            "kpi": Cr(self.cr),
            "ipt": Ipt(self.io),
            "aur": Aur(self.io),
            "apt": Apt(self.io)
        }

    def find_kpi(self, kpi):
        if kpi in self.key_figures:
            return self.key_figures[kpi]

        return Unknown(self.io)

class Cr:
    def __init__(self, io):
        self.io = io

    def laske(self):
        
        get_ly_cr = self._kpi_repository.get_cr(cr)
        

        cr_goal = cr_ly + {self.io}
