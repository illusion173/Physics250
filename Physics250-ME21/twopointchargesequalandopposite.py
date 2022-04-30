import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def findElectricField():
    
    charge = float(input("Input Charge: "))
    
    distance = float(input("Distance: "))
    
    x = float(input("X: "))
    
    final = (2 * k * charge * distance/((pow(pow(distance,2)+pow(x,2),1.5))))/1000000
    
    print(final)
    
    
findElectricField()