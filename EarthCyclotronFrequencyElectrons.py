import numpy as np
import math


def earthCyclotronFrequency():
    magneticField = input("Earth's Magnetic Field(ignore the x10^-4): ")
    magneticField = float(magneticField)
    magneticField = magneticField * pow(10,-4)
    #constants
    q = 1.6 * pow(10,-19)
    piMe = 2 * math.pi * 9.11 * pow(10,-31)
    cylotron = ((magneticField*q)/piMe)*pow(10,-6)
    print(cylotron)
earthCyclotronFrequency()