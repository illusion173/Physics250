import numpy as np
import math

def inducedCurrent():
    resistance = float(input('Input Resistance: '))
    mutualIndustance = float(input('Mutual Industance of coil and Solenoid in microH: '))
    mutualIndustance = mutualIndustance * pow(10, -5)
    amps = float(input('amps (A/s): '))
    
    inducedCurrent = amps * ((mutualIndustance)/(resistance))
    
    print(inducedCurrent)
    
inducedCurrent()