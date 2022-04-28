import numpy as np
import math


def findCurrentAftertime():
    
    resistor = float(input("Resistor: "))

    Faraday = float(input("Faraday microF: "))
    Faraday = Faraday * pow(10,-6)
    charge = float(input("Charge mC: "))
    charge = charge / 1000
    
    time = float(input("How much time in ms: "))
    time = time / 1000
    
    timeconstant = resistor * Faraday
    
    chargeNew = charge * (pow(math.e,-time/timeconstant))

    voltsNew = chargeNew/Faraday
    
    Amps = voltsNew/resistor
    print(Amps)
    
findCurrentAftertime()    