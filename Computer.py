class Computer:
    def __init__(self, manufacturer, model, price):

        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def __str__(self):
        return self.manufacturer.ljust(10)+self.model.ljust(10)+self.price.ljust(10)

    def __repr__(self):
        return "Manufacturer: ".ljust(20)+self.manufacturer.ljust(10)+"\n"+ "Model: ".ljust(20)+self.model.ljust(10)+"\n"+ "Price: ".ljust(20)+self.price.ljust(10)

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if int(price) > 10:
            self.__price = price
        elif price == 5:
            self.__price = None
        else:
            self.__price = 0
