import numpy as np
import math
# INCOMPLETE FUCKAAAAAAAAAAAAAA
extraNumber = 4 * math.pi * pow(10, -7)


def magField():
    velocity = float(input('Enter Velocity: '))
    ydistance = float(input('Y distance: '))
    xdistance = float(input('X distance: '))
    ZTesla = float(input('Input ZTesla: '))
    xdistance = xdistance / 1000
    ydistance = ydistance / 1000
    ZTesla = ZTesla * pow(10, -6)

    theta = math.asin(
        xdistance/(math.sqrt((pow(ydistance, 2)+pow(xdistance, 2)))))
   # theta = theta * (180 / math.pi)
    r = (math.sqrt((pow(ydistance, 2)+pow(xdistance, 2))))
 

magField()
