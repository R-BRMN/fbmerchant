#!/bin/python

from Computer import *
from Owner import *

def main():

    c1 = Computer("Lenovo", "x230", "550", "Intel3120M", "8")
    c2 = Computer("Lenovo", "x400", "250", "Intel3120M", "8")
    c3 = Computer("Dell", "9370", "1200", "Intel3120M", "8")
    c4 = Computer("Microsoft", "XBOX", "200", "Intel3120M", "8")

    s1 = Owner("Ronnies")

    s1.add_computer(c1)
    s1.add_computer(c2)
    s1.add_computer(c3)
    s1.add_computer(c4)

    print(str(s1))

    pass

if __name__ == "__main__":
    main()
