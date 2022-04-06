import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def findLengthSolenoid():
    turns = input("Input how many turns: ")
    turns = float(turns)
    current = input("Input current: ")
    current = float(current)
    magField = input("Input mag field: ")
    magField = float(magField)
    magField = magField/1000
    length = (extraNumber * turns * current)/magField
    length = length * 100
    print(length)

findLengthSolenoid()