import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def wavelength():
    MaxKE = float(input('Input MaxKE: '))
    WorkFunction = float(input('WorkFunction: '))

    MaxKE = MaxKE * electronConstant
    WorkFunction = WorkFunction * electronConstant
    
    partone = (MaxKE + WorkFunction)
    
    newLambda = (planck * speedofLight)/(partone)
    newLambda = newLambda * pow(10, 9)
    print(newLambda)
    print("In nm")
    
    
wavelength()