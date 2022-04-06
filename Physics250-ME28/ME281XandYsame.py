import numpy as np
import math

extraNumber = 1*pow(10,-5)

def num1calc():
    velocity = input("Input Velocity: ")
    velocity = float(velocity)
    velocity = velocity * 10000
    charge = input("Input Charge: ")
    charge = float(charge)
    charge = charge * .000001 
    x = input("X in cm: ")
    x = float(x)
    y = input("Y in cm: ")
    y = float(y)
    x = x/100
    y = y/100
    r = math.sqrt(pow(x, 2) + pow(y, 2))
    newX = x/r
    newY = y/r
    coordList = [newX, newY, 0]
    velocityList = [0,velocity, 0]
    result = np.cross(coordList, velocityList)
    B = (extraNumber * charge * result)/(pow(r,2))
    print(B)

num1calc()