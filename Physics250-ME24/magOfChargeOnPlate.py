import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def magofCharge():
    
    inner = float(input("Inner radius: "))
    outter = float(input("Outer radius: "))
    
    volts = float(input("Volts: "))
    
    cap = (inner * outter)/(k*(outter-inner))
    
    charge = volts * cap * pow(10,7)
    
    print(charge)
    
    
    
magofCharge()