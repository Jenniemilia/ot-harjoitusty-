class Store:
    """Myymälä joka käyttää sovellusta
    
    Attributes:
        storenumber: myymälän numerotunniste
        password: salasana
    """
    
    def __init__(self, storenumber, password):
        self.storenumber = storenumber
        self.password = password
