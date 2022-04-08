import numpy as np
import math

def findMaxCurrent():
    Henry = float(input('Input Henry: '))
    Faraday = float(input('Faraday: '))
    Charge = float(input('Charge: '))
    current = float(input('Current: '))
    #Conversions`
    Henry = Henry / 1000
    Faraday = Faraday * pow(10, -6)
    Charge =  Charge * pow(10, -6)
    current = current / 1000
    #Hold on to your pants this is a pain in the ass
    
    Energy = (.5 * (pow(Charge, 2)/(Faraday))) + (.5 * Henry * pow(current, 2))
    #note this is .5 * q^2/c + .5L*i^2
    Imax = math.sqrt((2*Energy)/Henry) * pow(10, 3)
    print(Imax)
    print("mA")
    
findMaxCurrent()