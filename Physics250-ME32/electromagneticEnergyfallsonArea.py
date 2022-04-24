import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 6 Type 
def MagneticField():
    Intensity = float(input("Input the EM wave intensity (W/m^2): "))
    length1 = float(input("Input the first length (m): "))
    length2 = float(input("Input the second length (m): "))
    time = float(input("Input the time (s): "))
    
    area = length1 * length2

    Energy = area * Intensity * time

    print("Electromagnetic energy that fell on the area:", Energy)
    
MagneticField()
