import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def storedoneachplate():
    capacitor = float(input("Input Capacitance "))
    Volts = float(input("Volts: "))    
    constant = float(input("Constant: "))
    
    answer = (constant * Volts * capacitor)/1000
    print(answer)
    
storedoneachplate()