import numpy as np
import math


def oscillationFreqMultiple():
    capacitor = float(input('Input Capacitor microF: '))
    Henry = float(input('Input Henry mH: '))
    Amount = float('Input Amount of Capacitors: ')
    frequency = (1/(2*math.pi*math.sqrt(Henry*pow(10,-3)*1*capacitor*pow(10,-6)))) * Amount

    print(frequency)    
    
oscillationFreqMultiple()