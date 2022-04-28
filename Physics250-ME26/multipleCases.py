import numpy as np
import math


def multiplecase():
    choice = float(input("Which Case? "))
    
    match choice:
        case 2:
            ampsone = float(input("Ampsone: "))
            ampsfour = float(input("Ampsfour: "))
            ampsfive = float(input("Ampsfive: "))
            ampsthree = ampsone-ampsfive-ampsfour
            print(ampsthree)
        case 3:
            ampsthree = float(input("Ampsthree: "))
            ampsfour = float(input("AmpsFour: "))
            ampsfive = float(input("AmpsFive: "))
            ampsone = ampsthree+ampsfour+ampsfive
            print(ampsone)
            
        case default:
            print("Please enter a case!")
    
    
multiplecase()