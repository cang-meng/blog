import random,time
def Sixteen():
    colorArr,color = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],''
    for i in range(6):
        color += colorArr[random .randint(0,14)]
    return "#"+color

def RGB(red=[0,255],green=[0,255],blue=[0,255]):
    return (random.randint(red[0],red[1]),random.randint(green[0],green[1]),random.randint(blue[0],blue[1]))

def EN():
    colorArr=['Red', 'orange' ,'yellow' ,'green' ,'blue' ,'purple','White']
    return colorArr[random.randint(0, len(colorArr)-1)]

def randNmae():
    return str(round(time.time()* 1000))+str(random.randint(1000,9999))
