import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def electricalEnergy():
    
    Faraday = float(input("Input Faraday: "))
    volts = float(input("Volts: "))
    constant = float(input("Constant: "))

    partone = .5 * Faraday * pow(volts, 2)
    
    final = partone/constant
    
    print(final)

    
    
    
electricalEnergy()
