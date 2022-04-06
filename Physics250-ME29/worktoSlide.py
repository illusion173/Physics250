import numpy as np
import math


#If you've found me I am the PS250 Easter Egg!
#Congrats for looking at the source code and learning the code a little bit!
#Good Luck!
def workWire():
    distance = float(input("Input distance apart (cm): "))
    resistance = float(input("Input the resistance (Ω): "))    
    magField = float(input(("Input the magnetic Field (T): ")))
    totalDistance = float(input("Input the total distance (cm): "))
    speed = float(input("Input the speed: "))
    distance = distance/100
    totalDistance = totalDistance/100
    work = ((pow(magField, 2) * speed * pow(distance, 2))/(resistance)) * totalDistance * 1000
    print(work)
    
    
    
workWire()