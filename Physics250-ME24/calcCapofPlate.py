import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def cap():
    area = float(input("Input Area: "))
    distance = float(input("Distance: "))
    distance = distance / 1000
    
    final = Esubo * (area/distance)
    
    final = final * pow(10,8)
    
    print(final)
    
cap()