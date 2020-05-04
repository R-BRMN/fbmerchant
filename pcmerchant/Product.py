from .Owner import *

class Product:

    FAKE_PRICE_INDICATOR = 20

    def __init__(self, name: str, price_as_advertised: int, owner: Owner, url: str):

        self.name = name
        self.price_as_advertised = price_as_advertised
        self.owner = owner
        self.url = url
        self.available = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price_as_advertised(self):
        return self.__price_as_advertised

    @price_as_advertised.setter
    def price_as_advertised(self, price_as_advertised):
        if price_as_advertised < self.FAKE_PRICE_INDICATOR:
            self.__price_as_advertised = None
        else:
            self.__price_as_advertised = price_as_advertised

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available):
        self.__available = available

    def __repr__(self):
        return str(self.__dict__)

    def markUnavailable(self):
        self.__available = False

        return "{_Product__name} {_Product__price_as_advertised} {_Product__owner} {_Product__url}".format(**self.__dict__)
