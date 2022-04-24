import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 4 Type 
def radPressure():
    ElecMagInt = float(input("Input the electromagnetic intensity (W/m^2): "))

    elecMax = math.sqrt(2*(ElecMagInt)*(4 * math.pi * pow(10,-7))*c)

    print("Max value of Electric Field in the Wave:", elecMax)
    
radPressure()
