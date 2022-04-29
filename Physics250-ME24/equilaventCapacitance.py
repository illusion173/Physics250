import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

#series
# 1/C = 1/C1 + 1/C2

#Parallel
#C = C1 + C2 + C3

def equivalentCap():
    
    decision = float(input("Input 1 Series, 0 for Parallel: "))
    
    if(decision == 1):
        capone = float(input("Enter Capacitance one: "))
        captwo = float(input("Enter Capacitance two: "))
        capthree = float(input("Enter Capacitance three: "))
        
        capacitance = 1/((1/capone) + (1/captwo) + (1/capthree))
        
    if(decision == 0):
        capone = float(input("Enter Capacitance one: "))
        captwo = float(input("Enter Capacitance two: "))
        capthree = float(input("Enter Capacitance three: "))
        
        capacitance = capone + captwo + capthree
    
    
    print(capacitance)

equivalentCap()