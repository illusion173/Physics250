import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)


def twocharges():
    
    firstcharge = float(input("First Charge: "))
    point = float(input("Point: "))
    secondCharge = float(input("Second Charge: "))
    
    firstpart = firstcharge / pow(point,2)
    
    secondPart = secondCharge / (firstpart)
    
    final = math.sqrt(secondPart) * -1
    
    print(final)
    
twocharges()