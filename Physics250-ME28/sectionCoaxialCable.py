import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def section():
    outRadius = input("Input outter radius: ")
    outRadius = float(outRadius)
    outRadius = outRadius/1000

    distance = input("Input distance: ")
    distance = float(distance)
    distance = distance/1000

    current1 = input("Input first Current: ")
    current2 = input("Input second Current: ")
    current1 = float(current1)
    current2 = float(current2)
    Ienclosed = current1 - current2

    if(distance < outRadius):
        Ienclosed = current1

    magField = abs((extraNumber/(2*math.pi*distance))*Ienclosed*pow(10,6))
    print(magField)

section()