import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)


def findEmf():
    lengthWire = float(input("Length of Wire (cm): "))
    speed = float(input("Enter Speed (m/s): "))
    firstT = float(input("Enter first microT: "))
    secondT = float(input("Enter second microT: "))
    lengthWire = lengthWire/100
    emf = secondT*speed*lengthWire
    print(emf)
    
    
    
findEmf()