import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 3 Type 
def waveIntensity():
    unit = input("Is it cm or mm?: ")
    if unit == "cm":
        wavelength = float(input("Input wavelength (cm): ")) / 100
    if unit == "mm":
        wavelength = float(input("Input wavelength (mm): ")) / 1000
    
    angfreq = c / wavelength * 2 * math.pi

    print("Angular Frequency:", angfreq / pow(10,9) ,"Grad/s" )
    
waveIntensity()
