import numpy as np
import math

def calcmagForce():
    diameter = input("Input diameter (cm): ")
    current = input("Input the Current (A): ")
    diameter = float(diameter)
    current = float(current)
    magneticFieldI = input("Magnetic Field i component: ")
    magneticFieldJ = input("Magnetic Field j component: ")
    vectorI = input("Input i component of vector: ")
    vectorJ = input("Input j component of vector: ")
    magneticFieldI = float(magneticFieldI)
    magneticFieldJ = float(magneticFieldJ)
    vectorI = float(vectorI)
    vectorJ = float(vectorJ)
    modifer = current * math.pi * pow((diameter/200),2)
    vector = np.array([vectorI*modifer,vectorJ*modifer])
    magneticField = np.array([magneticFieldI,magneticFieldJ]) 

    BxV = np.dot(magneticField,vector) 
    print(BxV* -1)

calcmagForce()