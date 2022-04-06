import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def introducedEMF():
    magField = input("Input the magnetic Field (T): ")
    turns = input("Input how many turns: ")
    E = input("Input the emf (V): ")
    omega = input("Input omega: ") 
    magField = float(magField)
    turns = float(turns)
    E = float(E)
    omega = float(omega)


    loopArea = (E)/(magField*turns*omega)
    print(loopArea*10000)

introducedEMF()
