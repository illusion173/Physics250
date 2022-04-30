import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def fluxDisk():
    
    radius = float(input("Radius: "))
    radius = radius /1000
    electricField = float(input("Electric Field: "))
    electricField = (electricField*pow(10,3))
    theta = float(input("Theta: "))
    
    actualTheta = 90-theta
    
    flux = math.cos(math.radians(actualTheta))*electricField*pow(radius,2) * math.pi
    
    print(flux)
    
fluxDisk()