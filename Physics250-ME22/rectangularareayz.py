import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def fluxrect():
    
    electricField = float(input("Electric Field: "))
    theta = float(input("Theta: "))
    area = float(input("Area of Rectangle: "))
    actualTheta = theta - 90
    flux = electricField * area * math.cos(math.radians(actualTheta))
    print(flux)
    
fluxrect()