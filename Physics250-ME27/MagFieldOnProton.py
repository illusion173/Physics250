import numpy as np
import math


def MagField():
    protonCharge = input("what is the proton charge (MeV): ")
    magForce = input ("What is the magnetic Force (pN): ")
    protonCharge = float(protonCharge)    
    magForce = float(magForce)

    #constants
    q = 1.6 * pow(10,-19)
    Mp = 1.67 * pow(10,-27)
    #continued
    protonCharge = protonCharge * pow(10,6)
    magForce = magForce * pow(10,-12)
    magField = magForce/(q* math.sqrt((2*q*protonCharge)/Mp))
    print(magField)
MagField()