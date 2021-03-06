#live graph of core temperature

import plotext as plt
import numpy as np
import subprocess as sub

bash = ["/opt/vc/bin/vcgencmd", "measure_temp"]
frames = 2  
l = 1000
dots = 10 

def getTemp():
    process = sub.Popen(bash, stdout=sub.PIPE)
    output, error = process.communicate()
    return output

def decodeTemp(output):
    temp = output[5:9]
    temp = temp.decode()
    ftemp = float(temp)
    return ftemp

def getDecodedTemp():
    return decodeTemp(getTemp())

def plotSetup():
    global x
    x = np.arange(1, l)
    xticks = np.linspace(1, l-1, dots)
    
    xlabels = [str(i) for i in range(dots)]


    plt.clf()
    plt.ylim(50, 70)
    plt.xticks(xticks, xlabels)
    plt.yticks([50, 55, 60, 65, 70])
    plt.plotsize(100, 30)
    plt.title("Temperature")
    plt.colorless()

def fillTemp(tempList):
    length = len(tempList)
    if length < dots:
        for i in range(dots):
            tempList.append(getDecodedTemp())

    elif length == dots:
        tempList.pop(0)
        tempList.append(getDecodedTemp())

    return tempList

def plot(y):
    plt.cld()
    plt.clt()
    plt.scatter(x, y, marker = "small", color = "artic", fillx = True)
    plt.sleep(0.05)
    plt.show()


def main():

    plotSetup()

    tempList =[]

    while True:
        tempList = fillTemp(tempList)
        y = tempList
        
        for i in range(frames):
            plot(y)

main()
