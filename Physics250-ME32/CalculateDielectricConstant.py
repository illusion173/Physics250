import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type
def Dielectric():
    propagation = float(input("Input the wave propagation (x10^8 m/s): ")) * pow(10,8)

    dielect = pow((c/propagation),2)

    print("Dielectric Constant:",dielect)
    
Dielectric()
