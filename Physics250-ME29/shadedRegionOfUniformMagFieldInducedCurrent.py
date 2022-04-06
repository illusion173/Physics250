from dis import dis
import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def solenoidRadius():
    magField = input("Input the value of B (T): ")
    speed = input("Input the speed (m/s): ")
    length = input("Input the length of the conduding loop L (cm): ")
    distance = input("Input the d of the conduding loop d (cm): ")
    resistance = input("Input the resistance of the conduding loop (Ω): ")
    decission = input("input whether or not it is dots or Xs: ")
    magField = float(magField)
    speed = float(speed)
    length = float(length)
    distance = float(distance)
    resistance = float(resistance)

    length = length/100
    distance = distance/100

    if decission == "dots":
        modifer = 1
    if decission == "X" or decission == "x":
        modifer = -1
    else:
        print("improper input for wheter it is Xs or dots")

    induCurrent = modifer * (magField * distance *speed)/resistance

    print(induCurrent)

solenoidRadius()
