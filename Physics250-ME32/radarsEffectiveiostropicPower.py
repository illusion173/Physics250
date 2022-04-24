import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 5 Type 
def waveIntensity():
    ElecField = float(input("Input frequency (x10^-2 V/m): ")) * pow(10,-2)
    radius = float (input("Input the Radius from center (km): ")) * 1000

    intensity = 4.001964365 * 0.5 * c * pow(ElecField,2) * e
    Power = intensity * math.pi * pow(radius, 2)

    print("Istropic Power:", Power / 1000 ,"KW" )
    
waveIntensity()
