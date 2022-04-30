import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)
chargeconstant = 1.602 * pow(10,-19)


def twopointcharges():
    
    
    chargeone = float(input("Charge One: "))
    
    chargetwo = float(input("Charge Two: "))
    
    rone = float(input("Rone: "))
    
    rtwo = float(input("Rtwo: "))
    
    partone = (chargeone*k)/(pow(rone,2))
    parttwo = (chargetwo*k)/(pow(rtwo,2))
    
    final = math.sqrt((pow(partone,2)+pow(parttwo,2)))/1000000000
    
    print(final)
    
    
    
    
twopointcharges()