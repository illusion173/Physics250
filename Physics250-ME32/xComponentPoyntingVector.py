import numpy as np
import math

c = 2.9979 * pow(10,8)
e = 8.85 * pow(10,-12)
#Practice test question 5 Type 
##NOT FINISHED
def waveIntensity():
    Elecmax = float(input("Input Emax (V/m): "))
    wavelength = float (input("Input the wavelength (m): "))
    t = float(input("Input t (𝜇s): ")) * pow(10,-6)

    omega = (c / wavelength) * 2 * math.pi
    E = Elecmax * math.cos(-1*t*omega)
    B = (Elecmax / c) * math.cos(-1*t*omega)
    s = 1/(4*math.pi* pow(10,-7)) * E *B


    print("X-Component of Poynting Vector:",  s )
    
waveIntensity()
