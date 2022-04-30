import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def externalForce():
    
    firstcharge = float(input("Input First Charge: ")) * pow(10,-6)
    secondcharge = float(input("Input Second Charge: ")) * pow(10,-6)
    distance = float(input("Input initial Distance: "))
    finaldistance = float(input("Input Final Distance: "))
    final = k * (firstcharge * secondcharge)/(finaldistance)
    initial = k * (firstcharge * secondcharge)/distance
    
    answer = final - initial
    
    answer = answer * 1000
    
    print(answer)
    
externalForce()
    
    
    