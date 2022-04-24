import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
def electronsEmerge():
    maxKE = float(input('Input Max KE: '))
    workFunction = float(input('Work Function: '))
    
    maxKE = maxKE * electronConstant
    workFunction = workFunction * electronConstant
    
    partone = (maxKE + workFunction)
    
    newLambda = (planck * speedofLight)/(partone)
    newLambda = newLambda * pow(10, 9)
    print(newLambda)
    print("In nm")
    
    
electronsEmerge()