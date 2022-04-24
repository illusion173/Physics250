import math
speedofLight = 2.9979*pow(10,8)

def spaceShipSpeed():
    firstLength = float(input('Input First Distance: '))
    secondLength = float(input('Input Second Distance: '))
    
    gamma = secondLength / firstLength
    
    partone = (1-pow((1/gamma),2)) * pow(speedofLight, 2)
    answer = math.sqrt(partone)
    
    answer = answer / speedofLight
    
    print(answer)

    
spaceShipSpeed()