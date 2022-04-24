import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 7 Type 
def radPressure():
    avgIntensity = float(input("Input the average intensity (W/m^2): "))
    absref = input("input absorbed or reflected: ")

    if absref == "absorbed" or absref == "Absorbed" or absref == "a" or absref == "A" :
        modifier = 1
    if absref == "reflected" or absref == "Reflected" or absref == "r" or absref == "R":
        modifier = 2
    else:
        print("improper choice, didnt put in absorbed or reflected")

    power = avgIntensity/c

    print("Average value of Radiation pressure:", power * modifier * pow(10,6) , "μPa")
    
radPressure()
