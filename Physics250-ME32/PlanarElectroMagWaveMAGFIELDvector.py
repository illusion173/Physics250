import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 2 Type 
def MagneticField():
    ElecMax = float(input("Input the Electric field j component (V/m): ")) 

    magneticField = (ElecMax/c) * pow(10,9)

    print("Magnetic Field:" , -1*magneticField , " nT")
    
MagneticField()
