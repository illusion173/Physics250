import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)
def speed():
    charge = input("Input charge: ")
    charge = float(charge)
    R = float(input("R on the X axis: "))
    R = R/1000
    magneticField = float(input("Magnetic field: "))
    velocity = ((4*math.pi * magneticField * pow(R,2))/(extraNumber*charge))/1000
    print(velocity)
    print("km/s")    
    




speed()