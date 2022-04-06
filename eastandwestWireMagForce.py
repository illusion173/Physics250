import numpy as np
import math 


extraNumber =  pow(10,-7)


def findCurrent():
    currentEast = input("Input current East: ")
    currentEast = float(currentEast)
    currentWest = input("Input current West: ")
    currentWest = float(currentWest)
    distance = input("Distance apart: ")
    distance = float(distance)
    distance = distance/100
    sectLength = input("Length of section:")
    sectLength = float(sectLength)
    
    forceMag = ((extraNumber*2*currentEast*currentWest)/distance)*sectLength
    forceMag = forceMag * pow(10,3)
    print(forceMag)



findCurrent()