import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def distanceequal():
    
    distance = float(input("Distance: "))
    electricField = float(input("Electric Field: "))
    secondElectricField = float(input("Second ElectricField: "))

    Z = electricField / secondElectricField
    
    answer = Z * distance
    
    print(answer)
    
distanceequal()
    