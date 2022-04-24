import math
speedofLight = 2.9979*pow(10,8)

def journeyinMinutes():
    speed = float(input('Input Speed relative to C: '))
    distance = float(input('Input Distance: '))
    speed = speed * speedofLight
    distance = distance * pow(10,12)
    gamma = math.sqrt(1/(1-pow((speed/speedofLight),2)))
    
    answer = distance / (gamma * speed)
    answer = answer / 60
    
    print(answer)
    print("In Minutes!")
    
journeyinMinutes()