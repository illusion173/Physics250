import numpy as np
import math 

def initialtorque():
    loops = input("Input number of Loops: ")
    length = input("Input the Length (m): ")
    width = input("Input the Width (m): ")
    current = input("Input current (A): ")
    magField = input("Input the magnetic field (T): ")
    angle0 = input("Input the first angle: ")
    angle1 = input("Input the second angle: ")
    loops = float(loops)
    current = float(current)
    length = float(length)
    width = float(width)
    magField = float(magField)
    angle0 = float(angle0)
    angle1 = float(angle1)

    area = length * width
    rotateWork = (math.cos(math.radians(angle1))-math.cos(math.radians(angle0)))*area*current*loops*magField
    print(rotateWork)
initialtorque()