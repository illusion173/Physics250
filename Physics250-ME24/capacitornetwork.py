import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

#series
# 1/C = 1/C1 + 1/C2

#Parallel
#C = C1 + C2 + C3
# if need charge in parallel only for a single capacitor, just do volts * capacitor

def capacitorNetwork():
    
    volts = float(input("Volts: "))
    
    capone = float(input("First Capacitor: "))
    captwo = float(input("Second Capacitor: "))
    capthree = float(input("Third Capacitor: "))
    
    decision = float(input("Series (1) Parallel (0): "))
    
    if decision == 1:
        partone = (1/capone) + (1/captwo) + (1/capthree)
        capTotal = 1/(partone)
        
    if decision == 0:
        capTotal = capone + captwo + capthree

    charge = capTotal * volts
    
    print(charge)
    capacitorchoice = float(input("Cap 1 (1), cap 2 (2), cap (3): "))
    
    match capacitorchoice:
        case 1:
            voltsone = charge / capone
            print("Volts")
            print(voltsone)
        case 2:
            voltTwo = charge / captwo
            print("Volts")
            print(voltTwo)
        case 3:
            voltsThree = charge / capthree
            print("Volts")
            print(voltsThree)
            
            
        case default:
            print("INPUT A VALID ENTRY")
    
    
    
capacitorNetwork()