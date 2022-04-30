import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)

def potentialatX():
    
    
    electricField = float(input("Electric Field: "))
    firstX = float(input("First X: "))
    firstVolts = float(input("First Volts: "))
    secondX = float(input("Second X: "))
    
    final = (electricField *(firstX-secondX)) + firstVolts
    
    print(final)
    
    
potentialatX()