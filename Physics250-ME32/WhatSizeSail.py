from os import access
import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 8 Type 
def MagneticField():
    Intensity = float(input("Intensity of the sun's electromagnetic radiation (W/m^2): "))
    mass = float(input("Input the mass of the spacecraft (kg): "))
    accceleration = float(input("Input the acceleration of the spacecraft (m/s^2): "))

    area = (mass * accceleration)/(2*(Intensity/c))

    print("sail area:", area / pow(1000,2) , "km^2")
    
MagneticField()
