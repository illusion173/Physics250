import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def electricFlux():
    
    linearcharge = float(input("Linear Charge: "))
    linearcharge = linearcharge * pow(10,-9)
    
    radius = float(input("Radius: "))/100
    
    flux = (linearcharge * 2 * radius)/Esubo
    
    print(flux)
    
electricFlux()