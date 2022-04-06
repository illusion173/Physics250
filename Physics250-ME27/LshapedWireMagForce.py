import numpy as np
import math


def Lwire():
    length = input("input the total length (m): ")
    current = input("Input the Current (A): ")
    magField = input("Input the Magnetic Field (T): ")
    length = float(length)    
    current = float(current)
    magField = float(magField)


    Force = (length * current * magField)/(math.sqrt(2))
    print(Force)
Lwire()