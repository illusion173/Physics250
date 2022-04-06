import numpy as np
import math

def turns():
    firstHenry = float(input('First Henry: '))
    secondHenry = float(input('Second Henry: '))
    
    firstHenry = firstHenry * pow(10,-5)
    secondHenry = secondHenry * pow(10,-3)
    
    turns = secondHenry/firstHenry
    
    print(turns)
    
    
turns()