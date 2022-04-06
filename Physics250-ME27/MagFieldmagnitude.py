import numpy as np
import math


def earthCyclotronFrequency():
    charge = input("Input the proton: ")
    magForce = input("Input Magnetic Force: ")
    charge = float(charge)
    magForce = float(magForce)
    charge = ((charge*pow(10,6))*1.6*pow(10,-19))
    magForce = magForce*pow(10,-12)
    #constants
    q = 1.6 * pow(10,-19)
    Me = 9.11 * pow(10,-31)
    cylotron = (magForce*1.67*pow(10,-27))/charge
    print(cylotron)
earthCyclotronFrequency()