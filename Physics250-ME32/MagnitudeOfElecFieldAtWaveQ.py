import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type
def ElectricField():
    typeclick = (input("micro or milli? : "))
    if typeclick == "micro":
        magField = float(input("Input the Magnetic Field (μT): ")) * pow(10,-6)
        elecField = (c * magField)
        
    if(typeclick == "milli"):
        magField = float(input("Input the Magnetic Field (mT): ")) * pow(10,-3)
        elecField = (c * magField) * pow(10,-6)

    print("Magnitude of the Electric Field:", elecField, "MN/C")
    
ElectricField()


