import numpy as np
import math 


extraNumber = 4 * math.pi * pow(10,-7)

def num2calc():
    Amps = input("Input Amps: ")
    Amps = float(Amps)
    lengthLegs = input("Input length of Legs: ")
    lengthLegs = float(lengthLegs)
    lengthLegs = lengthLegs/100
    midpointx = (0+lengthLegs)/2
    midpointy = (0+lengthLegs)/2
    distance = math.sqrt((pow(midpointx, 2)+pow(midpointy, 2)))
    MagField = (extraNumber * Amps)/(2*math.pi*distance) * pow(10,6)

    print(MagField)
num2calc()