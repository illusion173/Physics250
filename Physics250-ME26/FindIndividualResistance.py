import numpy as np
import math


def findIndividual():
    equilaventResistor = float(input("Input Equilavent Resistor: "))
    
    amountofResistor = float(input("Amount of Resistors: "))
    
    equilaventResistor = equilaventResistor * 1000

    final = equilaventResistor / amountofResistor
    print(final)    
        
    
findIndividual()
