from .Product import *

class Computer(Product):
    REPR_COLUMNS = [20,30,5]

    def __init__(self, name, price_as_advertised, owner, **specs):

        super().__init__(name, price_as_advertised, None, None)
        self.specs = specs

#    def __repr__(self):
#        repr_str = ''
#        table_data = list()
#
#        table_data.append(['','NAME','PRICE'])
#
#        for spec in self.specs:
#            table_data.append([spec.upper(), self.specs[spec]])
#
#        for row in table_data:
#            for col in range(len(row)):
#                repr_str += row[col].ljust(self.REPR_COLUMNS[col])
#            repr_str += '\n'
#        
#        return repr_str

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def price_as_advertised(self):
        return self.__price_as_advertised

    @price_as_advertised.setter
    def price_as_advertised(self, price_as_advertised):
        self.__price_as_advertised = price_as_advertised

