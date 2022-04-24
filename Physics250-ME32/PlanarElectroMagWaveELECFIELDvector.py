import numpy as np
import math

c = 2.9979 * pow(10,8)
#Practice test question 2 Type 
def MagneticField():
    MagField = float(input("Input the mag field I component (μT): ")) 

    ElecMax = MagField * c / 1000000 

    print("Electric Field:" , ElecMax )
    
MagneticField()
