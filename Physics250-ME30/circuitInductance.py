import numpy as np
import math


def cucuitInductance():
    resistance = float(input('Resistance: '))
    volts = float(input('Volts: '))
    current = float(input('Current (A/S): '))
    
    Inductance = (volts/(current)) * pow(10,3)
    print(Inductance)
    
cucuitInductance()
