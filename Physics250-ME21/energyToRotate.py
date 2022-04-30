import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)



def energytoRotate():
    Charge = float(input("Input Charge: "))
    Charge = Charge * pow(10,-9)
    distance = float(input("Distance: "))
    distance = distance/1000
    electricField = float(input("Electric Field: "))
    degreeone = float(input("Degree one: "))
    degreetwo = float(input("Degreetwo: "))
    
    Joules = Charge * distance * electricField * (math.cos(math.radians(degreeone)) - math.cos(math.radians(degreetwo)))
    
    print(Joules)
    
    
energytoRotate()
