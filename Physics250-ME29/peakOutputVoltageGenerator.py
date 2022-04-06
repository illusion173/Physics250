import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def introducedEMF():
    freq = input("Input the frequency (Hz): ")
    turns = input("Input how many turns of the squrare frame: ")
    area = input("Input the area  (m) (ignore the 10^-2): ")
    magField = input("Input magnetic Field Magnitude (T): ") 
    freq = float(freq)
    turns = float(turns)
    area = float(area)
    magField = float(magField)

    area = area * pow(10,-2)

    genVolt = freq * turns * area * magField * 2 * math.pi 
    print(genVolt)

introducedEMF()
