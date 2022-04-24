import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def findLifeTime():
    speed = float(input("Speed of light: "))
    time = float(input("Input MicroSec: "))
    speed = speed * pow(10,8)
    time = time * pow(10,-6)
    
    gamma = math.sqrt(1/(1-(pow((speed/speedofLight),2))))
    
    finalAnswer = time / gamma  
    print(finalAnswer)
    
findLifeTime()