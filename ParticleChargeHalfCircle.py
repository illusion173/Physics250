import numpy as np
import math


def flatRegionFlux():
    radius = input("Radius (cm): ")
    mass = input("Input the mass (ignore the 10^-12): ")
    speed = input("Input the speed (ignore the 10^3): ")
    magfield = input("Input magnetic field component (mT): ")    
    radius = float(radius)
    mass = float(mass)
    speed = float(speed)
    magfield = float(magfield)
    radius = radius/100
    mass = mass*pow(10,-12)
    speed = speed*pow(10,3)
    magfield = magfield/1000
    B = (mass*speed)/(magfield*radius)

    print(B*pow(10,6))
flatRegionFlux()