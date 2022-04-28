import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type
def MagneticField():
    unit = input("Is it final answer nano?: ")
    if unit == "yes": 
        ElecField = float(input("Input the magnitude of the Electric Field at Point P (N/C): ")) 
        MagField = (ElecField / c) * pow(10,6) * pow(10,2)
    else:
        ElecField = float(input("Input the magnitude of the Electric Field at Point P (N/C): ")) 
        MagField = (ElecField / c) * pow(10,6)
    print("Magnetic Field:", MagField , " μT")
    
MagneticField()
