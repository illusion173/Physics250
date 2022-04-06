import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def introducedEMF():
    magField = input("Input magnetic Field Magnitude (T): ")
    turns = input("Input how many turns of the squrare frame: ")
    sideL = input("Input the side length (cm): ")
    omega = input("Input the rpm: ")
    theta = input("Input the theta: ")
    magField = float(magField)
    turns = float(turns)
    sideL = float(sideL)
    omega = float(omega)
    theta = float(theta)

    sideL = sideL/100
    area = pow(sideL,2)
    ## omega = rads/time
    introEMF = turns*((magField*area*(math.cos(math.radians(theta))))*(omega*2*math.pi)/60)
    print(introEMF)

introducedEMF()
