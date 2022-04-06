import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def current():
    turns = input("Input how many turns: ")
    sideL = input("Input the length of the square side (cm): ")
    resistance = input("input the Resistance (Ω): ")
    angle = input("Input the angle: ")
    C = input("Input C (T/s^2): ")
    time = input("Input the time (s): ")
    turns = float(turns)
    sideL = float(sideL)
    resistance = float(resistance)
    angle = float(angle)
    C = float(C)
    time = float(time)

    B = 2*C*time
    area = pow(sideL/100,2)
    coilEMF = turns * area * B * math.sin(math.radians(angle))/resistance
    print(coilEMF)

current()
