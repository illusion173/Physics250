import numpy as np
import math


def circuitBreaker():
    print("If its 2-4 just input 0 when it asks for item 1 & 5.")

    limit = float(input("Input Limit: "))
    amps = float(input("Input Amps: "))
    itemone = float(input("Input item one: "))
    itemtwo = float(input("Input item two: "))
    itemthree = float(input("Input item three: "))
    itemfour = float(input("Input item four: "))
    itemfive = float(input("Input item five: "))
    
    voltsone = itemone / amps
    voltstwo = itemtwo / amps
    voltsthree = itemthree / amps
    voltsfour = itemfour / amps
    voltsfive = itemfive / amps
    
    final = voltsone + voltstwo + voltsthree + voltsfour + voltsfive
    
    if(final > limit):
        print("Too many volts therefore 0")
        
    if(final < limit):
        print(final)
    
    
    
    
    
    
        
    
    
    
    
circuitBreaker()