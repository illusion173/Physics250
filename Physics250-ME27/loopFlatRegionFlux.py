import numpy as np
import math


def flatRegionFlux():
    Area = input("Input the area (m^2): ")
    magfieldK = input("Input magnetic field K component (T): ")
    Area = float(Area)
    magfieldK = float(magfieldK)
    Flux = Area * magfieldK
    print(Flux)
flatRegionFlux()