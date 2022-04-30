import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def surfacechargedensity():
    
    distance = float(input("Input distance: ")) * pow(10,-3)
    
    volts = float(input("volts: ")) * pow(10,6)
    
    electricField = volts/distance
    
    final = electricField * Esubo * 1000
    
    print(final)
    
    
surfacechargedensity()