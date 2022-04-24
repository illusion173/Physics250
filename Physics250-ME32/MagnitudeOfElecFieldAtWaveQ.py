import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type
def ElectricField():
    magField = float(input("Input the Magnetic Field (μT): ")) * pow(10,-6)

    elecField = (c * magField) 

    print("Magnitude of the Electric Field:", elecField, "MN/C")
    
ElectricField()
