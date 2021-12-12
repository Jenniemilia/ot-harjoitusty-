class Budget:
    """Kuukauden budjetti.

    Attributes:
        storenumber = storenumber.
        sales_ly = last fiscal year sales.
        traffic = traffic in the store
        store_id = store identify number
    """

    def __init__(self, month, sales_ly, traffic, store_id):
        """Constructor that creates sales from previous years"""
        
        self.month = month
        self.sales_ly = sales_ly
        self.traffic = traffic
        self.store_id = store_id


