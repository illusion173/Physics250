import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)


def madeofTwoCharges():
    charge = float(input("Input Charge: "))
    
    distance = float(input("Distance between the two: "))
    
    ElectricField = float(input("Electric Field: "))
    
    
    final = charge * distance * ElectricField * pow(10,-2)
    
    print(final)
    
madeofTwoCharges()