import numpy as np
import math


def wireSegment():
    perpendicular = input("Is the quesion asking for a component perpendicular to the circle? Y or N: ")
    turns = input("How many Turns: ")
    radius = input("radius of the figure (cm): ")
    current = input("Current of the wire (A): ")
    rotate = input("Is the I arrow poining Clockwise or Counter Clockwise (C or CC): ")
    turns = float(turns)
    radius = float(radius)    
    current = float(current)
    radius = radius/100
    if rotate == "C":
        modifier = -1 
    if rotate == "CC":
        modifier = 1
    else:
        print("improper input for clockwise or counterclockwise")


    if (perpendicular == "Y"):
        perpcomponent = modifier*turns * pow(radius,2) * current * math.pi
    if (perpendicular == "N"):
        perpcomponent = 0
    else :
        print("improper input for if component is perpendicular")
    print(perpcomponent)
wireSegment()