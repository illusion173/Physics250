import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def solenoidRadius():
    magField = input("Input the value of B in B(t): ")
    elecField = input("Input the electric field outside the solenoid (V/m): ")
    distance = input("Input distance (m): ")
    magField = float(magField)
    elecField = float(elecField)
    distance = float(distance)


    radius = math.sqrt((2*elecField*distance)/magField)
    print(radius*100)

solenoidRadius()
