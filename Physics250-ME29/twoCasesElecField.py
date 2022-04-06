import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def introducedEMF():
    radius = input("Input radius: ")
    C = input("input the value of C: ")
    time = input("input the value of Time:")
    exponential = input("input the value of the exponential")
    radius = float(radius)
    C = float(C)
    time = float(time)
    exponential = float(exponential)

    case = input("input what case it is: ")
    if case == "1":
        modifier = 1
    if case == "2":
        modifier = -1
    else:
        print("improper choice of case")

    radius = radius/100
    area = math.pi * pow(radius,2)
    Bt = modifier * C *exponential * pow(time,(exponential-1))
    elecField = (area*Bt)/(2*math.pi*radius)
    print(elecField*-1000)

introducedEMF()
