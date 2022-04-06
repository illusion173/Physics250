import numpy as np
import math


def wireSegment():
    length = input("length of the wire (m): ")
    current = input("Current of the wire (A): ")
    magneticField = input("What is the Magnetic Field (T): ")
    direction = input ("What direction is the arrow I pointing (Left Or Right): ")
    length = float(length)    
    current = float(current)
    magneticField = float(magneticField)
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
    zcomponent = modifier * current *magneticField*length
    print(zcomponent/1.570783)
wireSegment()