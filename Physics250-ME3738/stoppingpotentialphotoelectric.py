import math
import wave
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def workFunctionWStoppingPotential():
    stoppingPotential = float(input("Input stopping Potential: "))
    wavelength = float(input("Input Wavelength: "))
    wavelength = wavelength * pow(10,-9)

    Kmax = stoppingPotential * electronConstant
    partone = (planck * speedofLight)/wavelength
    answer = partone - Kmax
    
    answer = answer/(electronConstant)
    print(answer)
    
    
workFunctionWStoppingPotential()