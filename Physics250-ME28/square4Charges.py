import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def square():
    sidelength = input("Input side Length: ")
    sidelength = float(sidelength)
    sidelength = sidelength/100
    current = input("Current: ")
    current = float(current)
    
    magneticField = (4*(extraNumber * current)/(2*math.pi * sidelength)) * pow(10, 4)
    print(magneticField)

square()