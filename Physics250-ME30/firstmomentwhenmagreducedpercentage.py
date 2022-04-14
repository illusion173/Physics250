import numpy as np
import math


def firstmomentreduced():
    faraday = float(input('Input Faraday: '))
    henry = float(input('Input Henry: '))
    percentage = float(input('Input Percentage: '))
    percentage = percentage / 100
    final = math.acos(percentage) * math.sqrt(faraday * henry) * pow(10,-3)
    print(final)
    
    
firstmomentreduced()
