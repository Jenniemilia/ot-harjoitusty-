class Budget:
    """Kuukauden budjetti.
    
    Attributes:
        storenumber = myymälä, jonka budjetti on kyseessä.
        budget = kuukauden budjetti.
        date = näyttää kyseisen päivän
    """
    
    def __init__(self, storenumber, budget, date):
        self.storenumber = storenumber
        self.budget = budget
        self.date = date

    