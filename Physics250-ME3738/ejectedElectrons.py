import math
speedofLight = 2.9979*pow(10,8)
electronConstant = 1.602 * pow(10, -19)
planck = 6.626 * pow(10,-34)
massOfElectron = 9.1093837 * pow(10,-31)

def ejectedElectrons():
    firstWaveLength = float(input("Input First Wave Length: "))
    secondWaveLength = float(input("Input Second Wave Length: "))
    first = 1240/firstWaveLength
    second = 1240/secondWaveLength
    finalAnswer = second - first
    
    print(finalAnswer)
    
    
ejectedElectrons()