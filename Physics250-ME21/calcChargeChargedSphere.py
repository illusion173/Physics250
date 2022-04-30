import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def chargedSphere():
    
    mass = float(input("Mass: "))
    ElectricField = float(input("Electric Field: "))
    
    force = mass * 9.8
    
    solution = (force / ElectricField) * 1000
    
    print(solution)
    
chargedSphere()