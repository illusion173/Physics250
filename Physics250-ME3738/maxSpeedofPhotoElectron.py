import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)


def maxSpeed():
    workFunction = float(input('Input Work Function: '))
    wavelength = float(input('Wavelength: '))
    workFunction = workFunction * electronConstant
    wavelength = wavelength * pow(10, -9)
    
    firstPart = ((planck * speedofLight)/(wavelength)) - workFunction
    
    secondPart = (2*firstPart)/(massOfElectron)
    finalAnswer = math.sqrt(secondPart)
    finalAnswer = finalAnswer/1000
    print(finalAnswer)
    print("In Km/s")
    
    
    
maxSpeed()