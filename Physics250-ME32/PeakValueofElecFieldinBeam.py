import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 6 Type 
def MagneticField():
    avgPower = float(input("Input the average power (mW): "))/1000
    radius = float(input("Input the radius (mm): "))/1000

    area = math.pi * pow(radius,2)

    intensity = avgPower/area
    elecField = math.sqrt(intensity*(2/(c * e)))

    print("Peak value of the Electric Field:", elecField)
    
MagneticField()
