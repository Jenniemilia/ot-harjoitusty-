class Kpi:
    """Luokka yksittäiselle avainluvulle.

    Attributes:
        cr: maksavien asiakkaiden osuus.
        ipt: myydyt kappaleet per ostostapahtuma.
        apt: keskiostossumma per ostostapahtuma.
        aur: keskihinta myydyille tuotteille.
    """

    def __init__(self, cr, ipt, apt, aur):

        self.cr = cr
        self.ipt = ipt
        self.apt = apt
        self.aur = aur

    def __str__(self):
        """Metodi, joka palauttaa olion nimen merkkijonona.

        Palauttaa olion merkkijonona"""
        return self.cr
        pass