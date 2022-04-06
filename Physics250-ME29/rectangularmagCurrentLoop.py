from more_itertools import first
import numpy as np
import math



def findMagofCurrent():
    turns = float(input("Input Turns: "))
    resistance = float(input("Resistance: "))
    Area = float(input("Area: "))
    firstT = float(input("First T in (mT): "))
    secondT = float(input("Second T in (mT): "))
    time = float(input("Input Seconds: "))
    
    firstT = firstT/1000
    secondT = secondT/1000
    current = (turns * Area * ((secondT - firstT)/time))/(resistance)
    print(current)
    
    
    
    
    
findMagofCurrent()