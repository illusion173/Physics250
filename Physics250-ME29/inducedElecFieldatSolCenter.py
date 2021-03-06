import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def solenoidRadius():
    radius = input("Input the radius (cm): ")
    magField = input("Input the value of magfield from B(t): ")
    distance = input("Input distance (cm): ")
    time = input("Input the time: ")
    constant = float(input("Input the constant near time _t: "))
    radius = float(radius)
    magField = float(magField)
    distance = float(distance)
    time = float(time)

    radius = radius/100
    distance = distance/100

    B = constant * magField * math.exp(constant*time)
    elecField = (pow(radius,2)*B)/(2*distance)
    print(elecField)

solenoidRadius()
