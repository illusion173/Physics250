import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def friendCrafSpeed():
    firstLength = float(input('First Length: '))
    secondLength = float(input('Second Length: '))
    
    gamma = firstLength/secondLength
    
    partone = (1-(pow((1/gamma),2))) * pow(speedofLight, 2)
    partwo = math.sqrt(partone)
    finalAnswer = partwo/speedofLight
    
    print(finalAnswer)
    
    
friendCrafSpeed()