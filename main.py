#!/bin/python
from pcmerchant.Computer import *
from pcmerchant.Owner import *
from pcmerchant.Product import *
from pcmerchant.Laptop import *

def main():


    c1 = Computer("Lenovo x240", 1400, "First Last", processor="i5-4300U 1.90Ghz", ram="4")
    c2 = Computer("Lenovo", "x400", "250")
    c3 = Computer("Dell", "9370", "1200")
    c4 = Computer("Microsoft", "XBOX", "200")


    c5 = Laptop("Lenovo", "T470", processor = "i5")


    o1 = Owner("Ronnies")
    o2 = Owner("P R")

    o1.add_computer(c1)
    o1.add_computer(c2)
    o1.add_computer(c3)
    o1.add_computer(c4)
    o2.add_computer(c5)


    p1 = Product("Thinkpad x230",20,'<ownerobject>','https://facebook.com/marketplace/example?=example')


    p1.markUnavailable()


    print (repr(c1))

if __name__ == "__main__":
    main()
