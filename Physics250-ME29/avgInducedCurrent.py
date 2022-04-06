import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def avgEMF():
    resistance = input("Input resistance (Ω): ") 
    magField = input("Input the Magnetic Field: ")
    radius0 = input("Input the first diameter value (cm): ")
    radius1 = input("Input the second diameter (cm): ")
    time = input("Input the time (s): ")
    decission = input("input whether or not it is dots or Xs: ")
    resistance = float(resistance)
    magField = float(magField)
    radius0 = float(radius0)
    radius1 = float(radius1)
    time = float(time)

    radius0 = radius0/200
    radius1 = radius1/200
    area0 = pow(radius0,2)*math.pi
    area1 = pow(radius1,2)*math.pi

    if decission == "dots":
        modifer = 1
    if decission == "X" or decission == "x":
        modifer = -1
    else:
        print("improper input for wheter it is Xs or dots")

    averageEMF =    modifer * (magField*(area0-area1))/(resistance*time )
    print(averageEMF)

avgEMF()
