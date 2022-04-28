import numpy as np
import math

c = 3 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 4 Type 
def waveIntensity():
    
    ElecField = float(input("Input frequency (kV/m): ")) * 1000

    intensity = 0.5 * c * pow(ElecField,2) * e

    print("Wavelength:", intensity / 1000 ,"KW/m^2" )
    
waveIntensity()
