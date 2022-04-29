import numpy as np
import math

#series
# 1/C = 1/C1 + 1/C2

#Parallel
#C = C1 + C2 + C3


Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def groupOfCapacitorsfour():
    
    volts = float(input("Volts: "))
    firstcap = float(input("First Capacitor: "))
    secondcap = float(input("Second Capacitor: "))
    thirdcap = float(input("Third Capacitor: "))
    fourthcap = float(input("Fourth Capacitor: "))
    
    
    partone = 1/((1/thirdcap)+1/(fourthcap))
    
    parttwo = partone + secondcap
    
    final = 1/((1/firstcap)+(1/parttwo))
    
    print(final)
    
groupOfCapacitorsfour()
    
