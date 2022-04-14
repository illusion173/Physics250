import numpy as np
import math


def oscillationFreq():
    capacitor = float(input('Input Capacitor microF: '))
    Henry = float(input('Input Henry mH: '))
    
    frequency = (1/(2*math.pi*math.sqrt(Henry*pow(10,-3)*1*capacitor*pow(10,-6))))

    print(frequency)    
    
oscillationFreq()