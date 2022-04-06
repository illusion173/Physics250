import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def uniformCurrent():
    current = input("Input current: ")
    current = float(current)
    diameter = input("Input diameter: ")
    diameter = float(diameter)
    diameter = diameter/1000
    distance = input("Input distance: ")
    distance = float(distance)
    distance = distance/1000
    radius = pow((diameter/2),2)

    magField = (extraNumber*current*distance)/(2*math.pi*radius) * pow(10,6)
    print(magField)



uniformCurrent()
