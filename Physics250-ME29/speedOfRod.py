import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def rodSpeed():
    mass = input("Input mass (g): ")
    resistance = input("Input the resistance (Ω): ")
    distance = input("Input distance apart (cm): ")
    magField = input("Input the magnetic Field (T): ")
    emf = input("Input the EMF (V): ")
    time = input("Input the time (s): ")
    mass = float(mass)
    resistance = float(resistance)
    distance = float(distance)
    magField = float(magField)
    emf = float(emf)
    time = float(time)
    distance = distance/100
    mass = mass/1000


    #speed = ((emf/(magField*distance)))
    #speed = (emf/(magField*distance)) * (1 - (pow(math.e, (-1* ((pow(distance,2) * pow(magField,2))/(mass*resistance))*time))))
    #speed = (math.exp(((pow(time,2)*pow(magField,2))/(mass*resistance))*time)) 
    #print(speed)

rodSpeed()
