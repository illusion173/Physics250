import math
speedofLight = 2.9979*pow(10,8)


def timeIntervalBlinks():
    time = float(input('Input Time (sec): '))
    speed = float(input('Speed: '))
    speed = speed * pow(10,8)
    
    
    gamma = math.sqrt(1/(1-pow((speed/speedofLight),2)))
    
    answer = gamma * time
    
    print(answer)
    
timeIntervalBlinks()
