import numpy as np
import math


def timeFindConstant():
    henry = float(input('Input Henry H: '))
    resistance = float(input('Resistance mOhms: '))
    
    constant = pow(10,3) * henry/(resistance)
    print(constant)
timeFindConstant()