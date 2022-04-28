import numpy as np
import math

def findVab():
    
    ampsone = float(input("Input ampsOne: "))
    ampsThree = float(input("InputampsThree: "))
    #ResistorOne = float(input("Resistor One: "))
    ResistorTwo = float(input("Resistor Two: "))
    #ResistorThree = float(input("Resistor Three: "))
    
    amps = ampsone - ampsThree
    Vab = ResistorTwo * amps
    
    print(Vab)
    
    
    
findVab()    