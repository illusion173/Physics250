import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)


def AlphaCentauriLy():
    firstLY = float(input("Input first LY: "))
    percent = float(input("Input percent: "))
    percent = percent / 100
    
    speed = percent * speedofLight
    
    gamma = math.sqrt(1/(1-(pow((speed/speedofLight),2))))
    
    finalAnswer = firstLY / gamma
    print(finalAnswer)
    
AlphaCentauriLy()