import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def numofTurns():
    magfield = input("Input magfield: ")
    magfield = float(magfield)
    magfield = magfield/1000
    current = input("Input current: ")
    current = float(current)
    radius = input("Input radius: ")
    radius = float(radius)
    radius = radius/100
    turns = ((2*math.pi*radius*magfield)/(extraNumber*current))
    print(turns)

numofTurns()