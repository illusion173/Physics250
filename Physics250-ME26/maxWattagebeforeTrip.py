import numpy as np
import math


def maxWattage():
    
    Watts = float(input("Wattage: "))
    amps = float(input("amps: "))
    volts = float(input("volts: "))
    
    voltsOne = Watts/amps
    
    voltsNew = volts-voltsOne
    
    final = voltsNew*amps
    
    print(final)
    
    
maxWattage()