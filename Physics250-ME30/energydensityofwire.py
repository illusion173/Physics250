import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)


def energydensityofWire():
    length = float(input('Input length: '))
    amps = float(input('Input Amps: '))
    length = length/100
    
    part1 = (extraNumber * amps)/(2*math.pi*length)
    
    part2 = ((pow(part1,2))/(2*extraNumber)) * pow(10,6)
    
    print(part2)
energydensityofWire()