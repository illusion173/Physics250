import numpy as np
import math


def longestTimeConstantLR():
    Henry = float(input('Input Inductor Henry: '))
    resistance = float(input('Input Resistance: '))
    count = float(input('How many resistors:  '))
    
    Henry = Henry / 1000
    constant = Henry * count
    final = constant/resistance
    final = final * pow(10,3)
    print(final)
    
    
longestTimeConstantLR()