import numpy as np
import math

def newCurrent():
    Henry = float(input('Input Henry H: '))
    resistance = (float(input('Input Resistance: ')))
    current = float(input('Current: '))
    time = float(input('Time (ms): '))
    time = time/1000
    timeconstant = Henry / resistance
    newCurrent = current * ((pow(math.e, (-time/timeconstant))))
    print(newCurrent)


    
newCurrent()