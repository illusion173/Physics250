import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def capacitorstore():
    area = float(input("Input Area: "))
    distance = float(input("Distance Seperation: "))
    electricfield = float(input("Electric Field: "))
    electricfield = electricfield * pow(10,6)
    
    final = (1/10000) * .5 * Esubo * pow(electricfield, 2) * area * distance
    print(final)
    
capacitorstore()