import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def introducedEMF():
    magField = input("Input the magnetic Field (T/s): ")
    radius = input("Input radius: ")
    magField = float(magField)
    radius = float(radius)

    loopArea = magField * math.pi * pow(radius,2)
    print(loopArea)

introducedEMF()
