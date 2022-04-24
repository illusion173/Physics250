import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def maxKEenergygivenJoules():
    workFunction = float(input('Work Function: '))
    #workFunction = workFunction * electronConstant
    PhotonEnergy = float(input('PhotonEnergy: '))
    PhotonEnergy = PhotonEnergy * pow(10,-18)
    PhotonEnergy = PhotonEnergy / electronConstant
    finalAnswer = PhotonEnergy - workFunction
    print(finalAnswer)




maxKEenergygivenJoules()