#live graph of core temperature

import plotext as plt
import numpy as np
import subprocess as sub

bash = ["/opt/vc/bin/vcgencmd", "measure_temp"]
frames = 20
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

def setup():
    global x
    x = np.arange(1, l)
    xticks = np.linspace(1, l-1, 10)
    
    xlabels = [str(i) for i in range(10)]


    plt.clf()
    plt.ylim(50, 70)
    plt.xticks(xticks, xlabels)
    plt.yticks([50, 60, 70])
    plt.plotsize(100, 30)
    plt.title("Temperature")
    plt.colorless()

def fillTemp(tempList):
    length = len(tempList)
    if length < dots:
        for i in range(10):
            tempList.append(getDecodedTemp())

    elif length == dots:
        tempList.pop(0)
        tempList.append(getDecodedTemp())

    return tempList

def plot(y):
    plt.cld()
    plt.clt()
    plt.scatter(x, y, marker = "dot")
    plt.sleep(0.05)
    plt.show()


def main():
    
    setup()

    tempList =[]

    while True:
        tempList = fillTemp(tempList)
        y = tempList
        
        #for i in range(frames):
        plot(y)

main()
