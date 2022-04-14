import numpy as np
import math

def maxInducedEMFOtherCoil():
    Henry = float(input('Input Henry: '))
    Amps = float(input('Input Amps: '))
    omega = float(input('Input omega rad/s: '))
    Henry = Henry / 1000
    volts = Henry * Amps * omega
    print(volts)
    
maxInducedEMFOtherCoil()
