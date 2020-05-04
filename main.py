#!/bin/python
from pcmerchant.Computer import *
from pcmerchant.Owner import *
from pcmerchant.Product import *

def main():

    print ("alright")
    print (Computer)

    c1 = Computer("Lenovo", "x230", "650")
    c2 = Computer("Lenovo", "x400", "250")
    c3 = Computer("Dell", "9370", "1200")
    c4 = Computer("Microsoft", "XBOX", "200")

    o1 = Owner("Ronnies")

    o1.add_computer(c1)
    o1.add_computer(c2)
    o1.add_computer(c3)
    o1.add_computer(c4)

    p1 = Product("Thinkpad x230",20,'<ownerobject>','https://facebook.com/marketplace/example?=example')

    print (p1.available)
    p1.markUnavailable()
    print (p1.available)
    
    print (repr(p1))

if __name__ == "__main__":
    main()
