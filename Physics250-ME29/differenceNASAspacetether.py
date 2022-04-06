import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def difference():
    length = input("Input length of the conducting wire (km): ")
    velocity = input("Input the velocity (m/s)(ignore the 10^3): ")
    magField = input("Input the perpendicular component of the magnetic field (ignore the 10^-5): ")
    length = float(length)
    velocity = float(velocity)
    magField = float(magField)


    length = length * 1000
    velocity = velocity * pow(10,3)
    magField = magField * pow(10,-5)
    ## omega = rads/time
    thetherDifference = length * velocity * magField * math.sin(math.radians(90))
    print(thetherDifference)

difference()
