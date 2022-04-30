import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def conductingRing():
    
    charge = float(input("Input Charge: "))
    
    radius = float(input("Radius: "))

    distance = float(input("Distance: "))
    
    electricField = ((k * charge * distance)/(pow(pow(radius,2)+pow(distance,2),3/2)))/100000
    
    print(electricField)
    
conductingRing()