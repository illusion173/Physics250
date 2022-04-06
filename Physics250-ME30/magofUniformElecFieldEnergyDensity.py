import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)
Esubo = 8.85 * pow(10,-12)

def inducedCurrent():
    magField = float(input('Input magField: '))
    
    electricField = magField/(math.sqrt(extraNumber * Esubo)) * pow(10, -6)
    
    print(electricField)
    
inducedCurrent()