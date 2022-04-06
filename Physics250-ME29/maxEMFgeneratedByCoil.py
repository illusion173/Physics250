import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def maximumEMF():
    loops = input("Input how many loops: ")
    radius = input("Input the radius (m): ")
    magField = input("Input magnetic Field Magnitude (T): ")
    turns = input("Input the turns per second: ")
    loops = float(loops)
    radius = float(radius)
    magField = float(magField)
    turns = float(turns)


    area = pow(radius,2)*math.pi
    rads = turns*2*math.pi
    ## omega = rads/time
    maxEMF = loops*area*magField*rads * pow(10,-4) * 10000
    print(maxEMF)

maximumEMF()
