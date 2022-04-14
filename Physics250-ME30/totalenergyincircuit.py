import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)

def totalenergy():
    henry = float(input('Input Henry: '))
    capacitance = float(input('Input Capacitance: '))
    charge = float(input('Input Charge: '))
    current = float(input('Input Current: '))
    
    henry = henry / 1000
    charge = charge * pow(10, -6)
    current = current / 1000
    capacitance = capacitance * pow(10, -6)
    energy = (((pow(charge, 2))/(2*capacitance)) + (.5 * henry * pow(current, 2))) * pow(10, 6)

    print(energy)
    
totalenergy()