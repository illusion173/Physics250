import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def torroidalSolenoid():
    turns = input("Input how many turns: ")
    turns = float(turns)
    current = input("Input current: ")
    current = float(current)
    distance = input("Input distance from center (cm): ")
    distance = float(distance)
    distance = distance/100
    magField = (extraNumber * turns * current)/(2*math.pi*distance)
    magField = magField*pow(10,3)
    print(magField)

torroidalSolenoid()
