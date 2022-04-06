import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def getMagField():
    current1 = input("Input loop current: ")
    current1 = float(current1)
    loopradius = input("Loop radius: ")
    loopradius = float(loopradius)
    distance = input("Distance: ")
    distance = float(distance)
    loopradius = loopradius/100
    distance = distance/100
    Magfield = (extraNumber * current1 * pow(loopradius, 2))/(pow(pow(distance, 2)+pow(loopradius, 2),1.5)*2) * pow(10,6)
    print(Magfield)




getMagField() 