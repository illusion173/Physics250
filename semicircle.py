import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def semicicle():
    length = input("Total Length: ")
    current = input("Input Current: ")
    length = float(length)
    current = float(current)
    #length = length/100
    radius = length/math.pi
    
    magneticField = .5 * ((extraNumber * current)/(2*radius))
    print(magneticField)



semicicle()