import numpy as np
import math 

extraNumber = 4 * math.pi * pow(10,-7)

def irregular():
    choice = input("Decide clockwise [0] or CC [1]")
    if(choice == '1'):
        print("Clockwise")
        print("Input line numbers")
        num1 = input("Amps 1: ")
        num1 = float(num1)
        direction = input("Input direction up or down: ")
        if(direction == 'down'):
            num1 = -1 * num1
        num2 = input("Amps 2: ")
        num2 = float(num2)
        direction = input("Input direction up or down: ")
        if(direction == 'down'):
            num2 = -1 * num2
        num3 = input("Amps 3: ")
        num3 = float(num3)
        direction = input("Input direction up or down: ")  
        if(direction == 'down'):
            num3 = -1 * num3
        Ienclosed = num1 + num2 + num3
        magField = extraNumber * Ienclosed
        print(magField)
    if(choice == '0'):
        print("Clockwise")
        print("Input line numbers")
        num1 = input("Amps 1: ")
        num1 = float(num1)
        direction = input("Input direction up or down: ")
        if(direction == 'up'):
            num1 = -1 * num1
        num2 = input("Amps 2: ")
        num2 = float(num2)
        direction = input("Input direction up or down: ")
        if(direction == 'up'):
            num2 = -1 * num2
        num3 = input("Amps 3: ")
        num3 = float(num3)
        direction = input("Input direction up or down: ")  
        if(direction == 'up'):
            num3 = -1 * num3
        Ienclosed = num1 + num2 + num3
        magField = extraNumber * Ienclosed
        print(magField)

irregular()