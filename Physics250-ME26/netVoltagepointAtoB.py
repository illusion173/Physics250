import numpy as np
import math


def pointBtoA():
    volts = float(input('volts: '))
    
    amps = float(input('amps: '))
    
    Resistance = float(input('Resistance: '))
    
    new = amps * Resistance * -1
    new = new-volts
    
    decision = float(input('Left (0) or right? (1): '))
    
    if(decision == 0):
        new = new * -1
    
    print(new)
    
    
    
pointBtoA()