import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)

def timeConstant():
    henry = float(input('Input Henry: '))
    ohms = float(input('Output Ohms: '))
    ohms = ohms / 1000
    timeConstant = henry/ohms
    
    print(timeConstant)
    
    
timeConstant()