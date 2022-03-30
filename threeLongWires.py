import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def getNumberCharge(): 
    y1 = input("Input first y: ")
    y1 = float(y1)
    y2 = input("Input second y: ")
    y2 = float(y2)
    y3 = input("Input third y: ")
    y3 = float(y3)
    I1 = input("Input amps one: ")
    I1 = float(I1)
    I2 = input("Input amps second: ")
    I2 = float(I2)
    I3 = input("Input amps third: ")
    I3 = float(I3)

    magField = ((extraNumber*I1)/(2*math.pi*y1) + (extraNumber*I2)/(2*math.pi*y2) - (extraNumber*I3)/(2*math.pi*y3))
    print(magField)

getNumberCharge()
