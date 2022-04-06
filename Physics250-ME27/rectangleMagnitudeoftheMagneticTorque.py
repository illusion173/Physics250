import numpy as np
import math 

def initialtorque():
    loops = input("Input number of Loops: ")
    length = input("Input the Length (m): ")
    width = input("Input the Width (m): ")
    current = input("Input current (A): ")
    magField = input("Input the magnetic field (T): ")
    angle = input("Input the angle: ")
    Bdirection = input("Input the direction of B (left or up): ")
    loops = float(loops)
    current = float(current)
    length = float(length)
    width = float(width)
    magField = float(magField)
    angle = float(angle)
    if Bdirection == "Left" or Bdirection == "left" or Bdirection == "L" or Bdirection == "l":
        modifier = 1
        #need to figure out what changes here still
    if Bdirection == "UP" or Bdirection == "Up" or Bdirection == "up" or Bdirection == "u":
        modifier = math.sin(math.radians(angle))
    else:
        print("didnt choose Left Or Up")

    area = length * width
    rotateWork = area*current*loops*magField*modifier
    print(rotateWork)
initialtorque()