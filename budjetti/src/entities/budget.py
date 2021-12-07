class Budget:
    """Kuukauden budjetti.

    Attributes:
        storenumber = myymälä, jonka budjetti on kyseessä.
        budget = kuukauden budjetti.
        date = näyttää kyseisen päivän
    """

    def __init__(self, month, sales_ly, traffic, store_id):
        self.month = month
        self.sales_ly = sales_ly
        self.traffic = traffic
        self.store_id = store_id


