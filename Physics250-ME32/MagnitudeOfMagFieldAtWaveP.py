import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type
def MagneticField():
    ElecField = float(input("Input the magnitude of the Electric Field at Point P (N/C): ")) 

    MagField = (ElecField / c) * pow(10,6)

    print("Magnetic Field:", MagField , " μT")
    
MagneticField()
