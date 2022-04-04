import numpy as np
import math


def perpSpeed():
    electricMag = input("input the electric magnitude (V/m): ")
    magneticfieldMag = input("Input the Magnetic Field (mT): ")
    electricMag = float(electricMag)    
    magneticfieldMag = float(magneticfieldMag)
    magneticfieldMag = magneticfieldMag/1000

    speed = electricMag / (magneticfieldMag)
    print(speed)
perpSpeed()