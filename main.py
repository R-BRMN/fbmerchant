#!/bin/python

from Computer import *
from Owner import *

def main():

    c1 = Computer("Lenovo", "x230", "550")
    c2 = Computer("Lenovo", "x400", "250")
    c3 = Computer("Dell", "9370", "1200")
    c4 = Computer("Microsoft", "XBOX", "200")

    s1 = Shop("Ronnies")


#    print(c1)
#    print(c2)
#    print(c3)

    s1.add_computer(c1)
    s1.add_computer(c2)
    s1.add_computer(c3)
    s1.add_computer(c4)
    print(str(s1))

    pass

if __name__ == "__main__":
    main()
