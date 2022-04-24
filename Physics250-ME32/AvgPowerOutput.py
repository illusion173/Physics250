import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 6 Type 
def waveIntensity():
    ElecField = float(input("Input frequency (V/m): ")) * pow(10,-2)
    radius = float (input("Input the distance from source (m): ")) 

    intensity = 4.001964365 * 0.5 * c * pow(ElecField,2) * e
    Power = intensity * math.pi * pow(radius, 2)

    print("Istropic Power:", Power *10000)
    
waveIntensity()
