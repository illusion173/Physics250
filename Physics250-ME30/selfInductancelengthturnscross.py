import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def selfInductantlengthcross():
    length = float(input('Length: '))
    numberofTurns = float(input('Number of turns: '))
    diameter = float(input('Diameter: '))
    
    radius = (diameter/100)/2
    
    length = length/100
    
    inductant = ((extraNumber * pow(numberofTurns, 2) * math.pi * pow(radius, 2))/(length)) * pow(10,3)
    
    print(inductant)
    
    
selfInductantlengthcross()