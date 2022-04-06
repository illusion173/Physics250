import numpy as np
import math


def cone():
    magfield = input("Input the magnetic field: ")
    diameter = input("Input diameter (m): ")
    height = input("Input height (m): ")
    magfield = float(magfield)
    diameter = float(diameter)
    height = float(height)
    angle = math.atan(height/(diameter/2))
    hype = math.sqrt(pow(height,2) + pow((diameter/2),2))
    coneArea = math.pi * (diameter/2) * hype
    coneFlux = coneArea * magfield * math.cos(angle)
    print(coneFlux)
cone()