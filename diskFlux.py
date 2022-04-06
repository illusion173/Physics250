import numpy as np
import math


def disc():
    magfield = input("Input the magnetic field: ")
    diameter = input("Input radius (m): ")
    angle = input("Input angle: ")
    magfield = float(magfield)
    radius = float(diameter)
    angle = float(angle)

    discArea = math.pi * pow(radius,2) 
    coneFlux = discArea * magfield * math.sin(math.radians(angle))
    print(coneFlux)
disc()