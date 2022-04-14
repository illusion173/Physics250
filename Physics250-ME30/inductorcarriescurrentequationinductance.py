import numpy as np
import math


#FIRST TAKE DERIVATIVE OF EQUATION
#plug in time
#thats the current
#divide the volts by current
#multiply by 10^3 = Answer
def whatInductance():
    firstCurrent = float(input('First Current (amps): '))
    time = float(input('Time (ms): '))
    time = time / 1000
    volts = float(input('Input Volts: '))
    volts = volts / 1000
    actualCurrent = firstCurrent * pow(math.e,(time/2))
    inductance = (volts)/actualCurrent
    print(inductance)
whatInductance()