import numpy as np
import math 

def initialtorque():
    loops = input("Input number of Loops: ")
    radius = input("Input Diameter (cm): ")
    current = input("Input current: ")
    magFieldX = input("Input the I component of B: ")
    radius = float(radius)
    loops = float(loops)
    current = float(current)
    magfieldX = float(magfieldX)
    radius = radius/200
    torque = loops * pow(radius,2) * math.pi * current * magFieldX 
    print(torque)
initialtorque()