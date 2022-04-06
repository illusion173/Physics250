import numpy as np
import math




def slidewireGen():
    d = float(input('Input d (cm): '))
    Resistance = float(input('Resistance : '))
    Force = float(input('Force: '))
    velocity = float(input('Velocity: '))
    d = d/100
    magField = math.sqrt((Force * Resistance)/(velocity))/d
    print(magField)





slidewireGen()