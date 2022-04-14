import numpy as np
import math

def shortestLRTime():
    
    henry = float(input('Henry: '))
    Count = float(input('Count of resistors: '))
    ohms = float(input('ohms: '))
    
    final = (henry/ohms)
    final = final / Count
    print(final)
shortestLRTime()