import math
speedofLight = 2.9979*pow(10,8)

def distanceinLY():
    percentage = float(input('Input percent: '))
    percentage = percentage / 100
    FirstDistanceGiven = float(input('First distance: '))
    speed = percentage * speedofLight
    gamma = math.sqrt(1/(1-pow((speed/speedofLight),2)))
    
    answer = gamma * FirstDistanceGiven
    
    print(answer)
    
distanceinLY()