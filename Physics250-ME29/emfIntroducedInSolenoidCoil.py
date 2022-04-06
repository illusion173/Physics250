import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def avgEMF():
    turnsM = input("Input how many turns/m: ")
    area0 = input("Input the solenoid area (m^2): ")
    B = input("Input B (A): ")
    C = input("Input C(A/s^2): ")
    turns = input("Input the turns of the coil: ")
    area1 = input("Input the coil area (m^2): ")
    time = input("Input the time (s): ")
    decision = input("Input whether inside or outside: ")
    turnsM = float(turnsM)
    area0 = float(area0)
    B = float(B)
    C = float(C)
    turns = float(turns)
    area1 = float(area1)
    time = float(time)

    if decision == "inside":
        C=C
    if decision == "outside":
        C=1
    else:
        print("improper decision")

    current = 2*C*time
    coilEMF = extraNumber*turns*turnsM*area1*current
    print(coilEMF)

avgEMF()
