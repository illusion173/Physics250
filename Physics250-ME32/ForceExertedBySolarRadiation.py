import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 8 Type 
def waveIntensity():
    Intensity = float(input("Input solar ratiation intensity (W/m^2): "))
    area = float (input("Input the area (m^2): "))

    force = 2* Intensity * area/c

    print("Force:", force  * pow (10,6),"μN" )
    
waveIntensity()
