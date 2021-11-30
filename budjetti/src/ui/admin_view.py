from tkinter import ttk, StringVar, constants


class AdminView:
    def __init__(self, root):
        self.root = root
        self._label_var = None
        pass

    
    def set_target(self):
        pass

    def convert_target(self):
        """Convert LY sales based on growth plan"""
        calculator = sales_ly * (growth_plan * 100)
 
        pass

    """Top-level widget on different stores?"""