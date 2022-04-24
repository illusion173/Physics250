import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 1 Type 
def MagneticField():
    dielecConst = float(input("Input the Dielectric Constant: ")) 

    Speed = (c / math.sqrt(dielecConst)) * pow(10,-8)

    print("Speed:", Speed , "x10^8 m/s")
    
MagneticField()
