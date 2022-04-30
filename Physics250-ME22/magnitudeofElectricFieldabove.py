import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def electricField():
    
    area = float(input("Input Area: "))
    
    charge = float(input("Charge: "))
    
    charge = charge * pow(10,-9)
    
    answer = (charge/area)/(2*Esubo)
    
    print(answer)
    
electricField()