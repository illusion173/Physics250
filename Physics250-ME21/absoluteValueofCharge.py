import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def absolutevalueofCharge():
    
    distance = float(input("Distance: "))
    
    
    Force = float(input("Force: "))
    
    final = math.sqrt((Force*pow(distance,2)/(k))) * pow(10,4)
    
    
    print(final)
    
absolutevalueofCharge()