import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def tetrehedron():
    
    enclosed = float(input("Enclosed charges: ")) * pow(10,-9)
    
    flux = (enclosed / (Esubo)) 
    
    print(flux)
    
    
tetrehedron()