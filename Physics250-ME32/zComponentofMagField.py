import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 2 Type 
def MagneticField():
    ElecMax = float(input("Input the Emax (V/m): ")) 
    angularVelocity = float(input("Input  (x10^6 Rad/s): ")) * pow(10,6)

    magneticField = (ElecMax/c) * pow(10,9)

    print("Magnetic Field:" , magneticField , " μT")
    
MagneticField()
