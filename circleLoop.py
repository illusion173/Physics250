import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def circleLoop():
    current1 = input("Input loop current: ")
    current2 = input("Input wire current: ")
    current1 = float(current1)
    current2 = float(current2)
    loopRadius = input("Input loop radius: ")
    loopRadius = float(loopRadius)
    distance = input("Input point P distance: ")
    distance = float(distance)
    part1 = (extraNumber * current1 * pow(loopRadius, 2))/(pow(pow(distance, 2)+pow(loopRadius, 2),1.5)*2) 
    part2 = (extraNumber * current2)/(2*math.pi*distance)
    part3 = math.sqrt((pow(part1,2)+pow(part2,2))) * pow(10,6)
    print(part3)

circleLoop()