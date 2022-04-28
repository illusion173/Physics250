import numpy as np
import math


def CurrentthroughResistor():
    
    volts = float(input("Volts: "))
    
    ResistorOne = float(input("Resistor One: "))
    ResistorTwo = float(input("Resistor Two: "))
    ResistorThree = float(input("Resistor Three: "))
    ResistorFour = float(input("Resistor Four: "))
    ResistorFive = float(input("Resistor Five: "))
    ResistorSix = float(input("Resistor Six: "))
    
    ResistorPartone = (ResistorOne*ResistorTwo)/(ResistorOne+ResistorTwo)
    ResistorPartTwo = ResistorThree + ResistorFour
    ResistorPartThree = (ResistorFive*ResistorSix)/(ResistorFive+ResistorSix)
    
    amps = volts/(ResistorPartone + ResistorPartTwo + ResistorPartThree)
    
    decision = input("Which Resistor? do the format: (ResistorOne) ")
    
    if(decision == "ResistorOne"):
        ResistorOneTwo = 1/(1/ResistorOne + 1/ResistorTwo)

        amps = (ResistorOneTwo * amps)/(ResistorOne)
        
        volts  = amps * ResistorOne
        print("Volts")

    if(decision == "ResistorTwo"):
        ResistorOneTwo = 1/(1/ResistorOne + 1/ResistorTwo)
        
        amps = (ResistorOneTwo * amps)/(ResistorTwo)
        
        
        volts  = amps * ResistorTwo  
        print("Volts")
        
    if(decision == "ResistorThree"):
        volts  = amps * ResistorThree        
        print("Volts")
        
    if(decision == "ResistorFour"):
        volts  = amps * ResistorFour        
        print("Volts")
        
    if(decision == "ResistorFive"):
        ResistorFiveSix = 1/(1/ResistorFive + 1/ResistorSix)
        
        amps = (ResistorFiveSix * amps)/(ResistorFive)

        volts  = amps * ResistorFive   
        print("Volts")
             
    if(decision == "ResistorSix"):
        ResistorFiveSix = 1/(1/ResistorFive + 1/ResistorSix)
        
        amps = (ResistorFiveSix * amps)/(ResistorSix)
        
        volts  = amps * ResistorSix
         
    print(amps)
    print("Amps")    
    print(volts)
    print("Volts")
    
CurrentthroughResistor()