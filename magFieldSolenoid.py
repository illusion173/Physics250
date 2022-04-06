import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def magFieldSolenoid():
    turns = input("Input how many turns: ")
    turns = float(turns)
    current = input("Input current: ")
    current = float(current)
    length = input("Input length (cm): ")
    length = float(length)
    length = length/100
    magField = (extraNumber * turns * current)/length
    print(magField)

magFieldSolenoid()
