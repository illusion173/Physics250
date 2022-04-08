import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)

def energyDensity():
    amps = float(input('Amps: '))
    diamater = float(input('Diamater: '))
    diamater = diamater / 100
    radius = diamater / 2
    
    energyDensity = (extraNumber * pow(amps, 2))/(8*pow(radius, 2))
    print(energyDensity)
    
    
    
energyDensity()