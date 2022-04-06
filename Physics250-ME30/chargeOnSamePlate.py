import numpy as np
import math
extraNumber = 4 * math.pi * pow(10,-7)
Esubo = 8.85 * pow(10,-12)


def samePlate():
    Henry = float(input('Input Henry (mH): '))
    Faraday = float(input('Input Faraday: '))
    Charge = float(input('Input Charge: '))
    time = float(input('Input time: '))
    #Conversions dont mind me
    Henry = Henry / 1000
    Faraday = Faraday * pow(10, -6)
    Charge = Charge * pow(10, -9)
    time = time / 1000
    #Quick note, if youre doing this with a calculator, ensure youre in radians mode!
    #Math.cos automatically assumes radian input
    #pow(10,9) is for conversions and reader legibility.
    newCharge = pow(10, 9) *Charge * math.cos((time)/(math.sqrt(Henry*Faraday)))
    
    print(newCharge)
    
samePlate()