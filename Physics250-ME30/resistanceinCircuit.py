import numpy as np
import math

def resistanceinaCircuit():
    henry = float(input('Input Henry: '))
    volts = float(input('Volts: '))
    percentage = float(input('Percentage (Dont put %): '))
    seconds = float(input('Seconds: '))
    
    percentage = percentage / 100
    actualdecimal = 1 - percentage
    naturallog = math.log(actualdecimal)
    
    finalanswer = (naturallog * henry)/(seconds) * -1
    print(finalanswer)
    
resistanceinaCircuit()