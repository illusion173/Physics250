import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)



def energyDensityMagFieldCenter():
    current = float(input('Enter Current: '))
    diameter = float(input('Diameter: '))
    radius = (diameter / 100)/2
    
    Density = (extraNumber * pow(current,2))/(8*pow(radius, 2))
    
    print(Density)
    
    
    
energyDensityMagFieldCenter()