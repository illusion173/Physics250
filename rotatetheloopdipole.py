import numpy as np
import math 

def rotatework():
    diameter = input("Input the diameter (mm): ")
    current = input("Input current (A): ")
    magField = input("Input the magnetic Field (T): ")
    diameter = float(diameter)
    current = float(current)
    magField = float(magField)
    diameter = diameter/1000
    work = pow(diameter,2) * math.pi * current * magField * 0.5
    print(work)
rotatework()