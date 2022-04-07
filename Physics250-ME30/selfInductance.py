import numpy as np
import math


def selfInductance():
    firstAmp = float(input('First Amps: '))
    firstrads = float(input('First Rads/second: '))
    volt = float(input('Volts: '))
    
    max = firstAmp * firstrads
    Henry = (volt / max) * 1000
    print(Henry)
    print("mH")
    
    
        
selfInductance()