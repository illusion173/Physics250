import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def findExcess():
    
    electricCharge = float(input("Input ElectricCharge:"))
    
    final = electricCharge / 1.602
    
    final = final * 10
    
    print(abs(final))
    
findExcess()