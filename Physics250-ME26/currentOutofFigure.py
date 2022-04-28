import numpy as np
import math


def findCurrent():
    Volts = float(input("Input Volts: "))
    
    Resistorone = float(input("Resistor one: "))
    ResistorTwo = float(input("Resistor two: "))
    ResistorThree = float(input("Resistor three: "))
    
    TotalResistance = 1/Resistorone + 1/ResistorTwo + 1/ResistorThree
    TotalResistance = 1/(TotalResistance)
    
    amps = Volts/TotalResistance
    
    print(amps)
    
findCurrent()