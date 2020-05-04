from Product import *

class Computer(Product):

    def __init__(self, price_as_advertised, motherboard, ram):

        self.motherboard = motherboard
        self.ram = ram
        self.price_as_advertised = price_as_advertised

    def __str__(self):
        return self.manufacturer.ljust(10)+self.model.ljust(10)+self.price_as_advertised.ljust(10)

    def __repr__(self):
        return "Manufacturer: ".ljust(20)+self.manufacturer.ljust(10)+"\n"+ "Model: ".ljust(20)+self.model.ljust(10)+"\n"+ "Price: ".ljust(20)+self.price_as_advertised.ljust(10)

    def __iter__(self):
        for i in self.__dict__:
            yield self.__dict__[i]

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
