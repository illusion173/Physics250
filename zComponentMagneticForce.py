import numpy as np
import math


def wireSegment():
    length = input("length of the wire (m): ")
    current = input("Current of the wire (A): ")
    magneticField = input("What is the Magnetic Field (T): ")
    angle = input("what is the Angle: ")
    direction = input ("What direction is the arrow I pointing (Left Or Right): ")
    length = float(length)    
    current = float(current)
    magneticField = float(magneticField)
    angle = float(angle)
    #constants
    q = 1.6 * pow(10,-19)
    Me = 9.11 * pow(10,-31)
    #continued
    if direction == "Left" or direction == "left" or direction == "L" or direction == "l":
        modifier = 1
    if direction == "Right" or direction == "right" or direction == "R" or direction == "r":
        modifier = -1
    else:
        print("didnt choose Left Or Right")
    zcomponent = modifier * current * (length*np.cos(np.radians(angle)))*magneticField
    print(zcomponent)
wireSegment()