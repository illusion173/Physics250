import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
    
    
    
def parralelFindCharge():
    volts = float(input("Volts: "))
    
    capone = float(input("First Capacitor: "))
    captwo = float(input("Second Capacitor: "))
    capthree = float(input("Third Capacitor: "))
    
    capTotal = capone + captwo + capthree

    charge = capTotal * volts
    
    capacitorchoice = float(input("Cap 1 (1), cap 2 (2), cap (3): "))

    
    match capacitorchoice:
        case 1:
            finalCharge = charge * (capone/capTotal)
            print(finalCharge)
            
        case 2:
            finalCharge = charge * (captwo/capTotal)
            print(finalCharge)
        case 3:
            finalCharge = charge * (capthree/capTotal)
            print(finalCharge)
            
        case default:
            print("INPUT A VALID ENTRY")
    
    
    
parralelFindCharge()