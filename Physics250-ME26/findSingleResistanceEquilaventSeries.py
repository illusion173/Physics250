import numpy as np
import math
# Series
# Resistance = resistor1 + resistor2 + resistorn...

#parallel 1/R = 1/R1 + 1/R2

def resistanceCalc():
    firstResistor = float(input("Resistance one: "))
    secondResistor = float(input("Resistance two: "))
    
    final = firstResistor + secondResistor
    
    print(final)
    
resistanceCalc()