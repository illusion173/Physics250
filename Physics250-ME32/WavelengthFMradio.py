import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 3 Type 
def WaveLength():
    Frequency = float(input("Input frequency (MHz): ")) * 1000000

    length = c / Frequency

    print("Wavelength:", length )
    
WaveLength()
