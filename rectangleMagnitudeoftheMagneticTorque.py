import numpy as np
import math 

def initialtorque():
    loops = input("Input number of Loops: ")
    length = input("Input the Length (m): ")
    width = input("Input the Width (m): ")
    current = input("Input current (A): ")
    magField = input("Input the magnetic field (T): ")
    angle = input("Input the angle: ")
    loops = float(loops)
    current = float(current)
    length = float(length)
    width = float(width)
    magField = float(magField)
    angle = float(angle)


    area = length * width
    rotateWork = math.sin(math.radians(angle))*area*current*loops*magField
    print(rotateWork)
initialtorque()