import numpy as np
import math 


extraNumber = 4 * math.pi * pow(10,-7)


def findCurrent():
    current = input("Input current: ")
    distance = input("Distance: ")
    linerMassDensity = input("Liner Mass Density: ")
    current = float(current)
    distance = float(distance)
    linearMassDensity = float(linerMassDensity) 
    distance = distance/100
    linearMassDensity = linearMassDensity * pow(10, -4)


    current2 = ((linearMassDensity * 9.8 * 2 * math.pi * distance)/(extraNumber*current))*10
    print(current2)



findCurrent()