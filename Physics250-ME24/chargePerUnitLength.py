import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def chargePerUnitLength():
    
    first = float(input("First radii: "))
    
    second = float(input("Second radii: "))
    
    volts = float(input("Volts: "))
    
    top = (2*math.pi * Esubo)/(np.log(second/first))
    
    final = volts * top * pow(10,9)
    
    print(final)
    
    
chargePerUnitLength()