import numpy as np
import math

def calcmagForce():
    charge = input("Input charge: ")
    charge = float(charge)
    velocityI = input("Input i component of velocity: ")
    velocityJ = input("Input j component of velocity: ")
    velocityK = input("Input k component of velocity: ")      
    magneticFieldI = input("Magnetic Field i component: ")
    magneticFieldJ = input("Magnetic Field j component: ")
    magneticFieldK = input("Magnetic Field k component: ")
    velocityI = float(velocityI)
    velocityJ = float(velocityJ)
    velocityK = float(velocityK) 
    magneticFieldI = float(magneticFieldI)
    magneticFieldJ = float(magneticFieldJ)
    magneticFieldK = float(magneticFieldK) 
    magneticField = np.array([magneticFieldI*1000,magneticFieldJ*1000,magneticFieldK*1000])
    velocity = np.array([velocityI,velocityJ,velocityK])
    BxV = np.cross(magneticField,velocity)
    BV = np.linalg.norm(BxV)
    magForce = BV*(charge*1.6*pow(10,-19))
    print(magForce*pow(10,12))

calcmagForce()