import numpy as np
import math


def wireSegment():
    electricField = input("what is the Electric Field (V/m): ")
    MagneticField = input ("What is the magnetic field (mT): ")
    radius = input("Input the Radius (cm): ")
    charge = input("Input the Charge (e): ")
    electricField = float(electricField)    
    MagneticField = float(MagneticField)
    radius = float(radius)
    charge = float(charge)

    #constants
    q = 1.6 * pow(10,-19)
    #continued
    MagneticField = MagneticField/1000
    radius = radius/100


    mass = (MagneticField*radius*charge*q)/(electricField/MagneticField)
    print(mass)
wireSegment()