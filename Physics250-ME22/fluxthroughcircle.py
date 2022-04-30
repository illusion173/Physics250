import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def fluxthroughcircle():
    
    electricField = float(input("Electric Field: "))
    radius = float(input("Radius: "))
    
    flux  = electricField * math.pi * pow(radius,2)
    print(flux)
    
fluxthroughcircle()