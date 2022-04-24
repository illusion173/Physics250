import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)


def findMavisTime():
    speed = float(input('Speed of Light: '))
    distance = float(input('Distance: '))
    
    speed = speed * speedofLight
    distance = distance * pow(10,9)
    
    gamma = math.sqrt(1/(1-(pow((speed/speedofLight),2))))
    
    finalAnswer = distance / (speed*gamma)
    print(finalAnswer)
    
    
    
findMavisTime()