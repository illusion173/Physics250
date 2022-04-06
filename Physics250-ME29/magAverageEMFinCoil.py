import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def avgEMF():
    turns = input("Input how many turns: ")
    radius = input("Input the radius (cm):")
    resistance = input("Input resistance (Ω): ")
    magField0 = input("Input the first magnetic Field value (T): ")
    magField1 = input("Input the second magnetic Field value (T): ")
    time = input("Input the time (s): ")
    turns = float(turns)
    radius = float(radius)
    resistance = float(resistance)
    magField0 = float(magField0)
    magField1 = float(magField1)
    time = float(time)
    radius = radius/100

    area = pow(radius,2)*math.pi
    averageEMF = turns * area * ((magField1-magField0)/time)
    print(averageEMF)

avgEMF()
