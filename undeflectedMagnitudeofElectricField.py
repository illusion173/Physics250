import numpy as np
import math


def earthCyclotronFrequency():
    difference = input("potential difference (kV): ")
    magneticField = input("magnetic Field value (micro T): ")
    magneticField = float(magneticField)
    difference = float(difference)
    difference = difference*1000
    magneticField = magneticField * pow(10,-6)
    #constants
    q = 1.6 * pow(10,-19)
    Me = 9.11 * pow(10,-31)
    #continued
    sqrtV = math.sqrt((difference* q)/(0.5*Me))
    electricField = sqrtV*magneticField
    print(electricField)
earthCyclotronFrequency()