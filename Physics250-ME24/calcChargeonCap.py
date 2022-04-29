import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def calcCharge():
    
    faraday = float(input("Input Faraday: "))
    volts = float(input("Input Volts: "))
    
    charge = faraday * volts

    
    print(charge)
    

calcCharge()