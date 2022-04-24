import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)


def maxKE():
    workFunction = float(input('Work Function: '))
    PhotonEnergy = float(input('PhotonEnergy: '))
    
    #workFunction = workFunction * electronConstant
    #PhotonEnergy = PhotonEnergy * electronConstant
    
    finalAnswer = PhotonEnergy - workFunction
    finalAnswer = finalAnswer * electronConstant
    print(finalAnswer)
    print("Take the first 2 digits.")
    
    

    
maxKE()