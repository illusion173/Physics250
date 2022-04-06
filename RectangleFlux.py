import numpy as np
import math


def magneticFlux():
    dimensionX = input("Input the first area Dimension(km): ")
    dimensionY = input("Input the second area Dimension(km): ")
    angle = input("Input the angle: ")
    magneticField = input("input the magnetic field (nT):")
    dimensionX = float(dimensionX)
    dimensionY = float(dimensionY)
    angle = float(angle)
    magneticField = float(magneticField)
    magneticField = magneticField*pow(10,-9) 
    angle =np.sin(np.radians(angle))
    area = (dimensionX*1000)*(dimensionY*1000) 
    magFlux = area*magneticField*angle
    print(magFlux)
magneticFlux()