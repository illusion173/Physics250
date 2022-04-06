import numpy as np
import math 

def initialtorque():
    loops = input("Input number of Loops: ")
    radius = input("Input Diameter (cm): ")
    current = input("Input current (A): ")
    magField = input("Input the magnetic field (T): ")
    angle = input("Input the given angle: ")
    radius = float(radius)
    loops = float(loops)
    current = float(current)
    magField = float(magField)
    angle = float(angle)
    radius = radius/200
    torque = loops * pow(radius,2) * math.pi * current * magField * math.cos(math.radians(angle))
    print(torque)
initialtorque()