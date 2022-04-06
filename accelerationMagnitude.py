import numpy as np
import math 

def accelerationMag():
    velcoity = input("Input velocity: ")
    magField = input("Input the magnetic field (nT): ")
    angle = input("Input the angle: ")
    velocity = float(velcoity)
    magField = float(magField)
    angle = float(angle)

    magField = magField * pow(10,-9)

    #consants 
    q = 1.6 * pow(10,-19)
    Me = 9.11 * pow(10,-31)

    acceleration = (math.sin(math.radians(angle))*velocity*q*magField)/Me
    print(acceleration*pow(10,-6))
accelerationMag()