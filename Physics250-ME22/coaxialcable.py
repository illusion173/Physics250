import numpy as np
import math

Esubo = 8.854 * pow(10,-12)
k = 8.988 * pow(10,9)


def magofElectricField():
    
    linearone = float(input("Input Linear Inner: ")) * pow(10,-9)
    
    lineartwo = float(input("Input Linear Outter: ")) * pow(10,-9)
    
    distance = float(input("Distance from central axis: ")) * pow(10, -2)
    
    electricfield = (linearone + lineartwo)/(2*math.pi*Esubo*distance)
    
    
    print(electricfield)
    
magofElectricField()    