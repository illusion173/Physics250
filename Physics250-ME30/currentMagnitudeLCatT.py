import numpy as np
import math


def currentMagnitude():
    henry = float(input('Input Henry: '))
    capacitor = float(input('Capacitor: '))
    charge = float(input('Charge: '))
    time = float(input('Time: '))
    
    henry = henry / 1000
    capacitor = capacitor * pow(10, -6)
    charge = charge / 1000
    time = time / 1000
    
    omega = 1/(math.sqrt(henry * capacitor))
    outside = omega * charge
    inside = omega * time
    sinfunc = math.sin(inside)
    current = abs(outside * sinfunc)
    #current = abs(omega * charge * math.sin(math.radians(inside)))
    print(current)
    
    
currentMagnitude()