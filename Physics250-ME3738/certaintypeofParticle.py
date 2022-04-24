import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)


def averageLiftimeAsMeasuredBysomeone():
    speed = float(input("Input Speed of particle: "))
    averagelifetime = float(input("Average liftime: "))
    speed = speed * pow(10,8)
    averagelifetime = averagelifetime * pow(10,-6)
    gamma = math.sqrt(1/(1-(pow((speed/speedofLight),2))))
    
    finalAnswer = gamma * averagelifetime * pow(10,6)
    
    print(finalAnswer)
    
averageLiftimeAsMeasuredBysomeone()