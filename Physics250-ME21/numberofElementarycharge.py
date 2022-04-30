import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)

def numberofCharge():
    charge = float(input("Input Charge: "))
    charge = charge * pow(10,6)
    time = float(input("Time: "))
    
    number = (time * charge)/(chargeconstant)
    
    print(number)
                    
numberofCharge()