import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def potentialofCube():
    
    magnitudeofCharge = float(input("Input magnitude of charges: "))
    positive = float(input("Positive Total: "))
    sidelength = float(input("Sidelength: "))
    
    distance = (sidelength * math.sqrt(3))/2
    
    final = ((positive * k * magnitudeofCharge)/distance) * pow(10,-9)
    
    print(final)
    
potentialofCube() 
