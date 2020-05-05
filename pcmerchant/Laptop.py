from .Computer import *

class Laptop(Computer):
    
    def __init__(self, manufacturer, model, **specs):
        self.name = f"{manufacturer} {model}"
        self.specs = specs

    def __repr__(self):
        repr_str = ''
        for spec in self.specs:
            repr_str += spec
        return repr_str
