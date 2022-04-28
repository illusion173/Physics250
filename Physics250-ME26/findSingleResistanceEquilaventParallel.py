import numpy as np
import math
# Series
# Resistance = resistor1 + resistor2 + resistorn...
# Current = Same for each part in Series
# Volts = V1 + V2 + V3 + V4

# Parallel 
# 1/R = 1/R1 + 1/R2
# Voltage = Same for all
# Current = I1 + I2 

def resistanceCalc():
    firstResistor = float(input("Resistance one: "))
    secondResistor = float(input("Resistance two: "))
    
    final = 1/(1/firstResistor + 1/secondResistor)
    
    print(final)
    
resistanceCalc()