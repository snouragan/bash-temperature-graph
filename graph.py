#live graph of core temperature

import plotext as plt
import numpy as np
import subprocess as sub

bash = ["/opt/vc/bin/vcgencmd", "measure_temp"]

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


l, n = 1000, 2
x = np.arange(0, l)
xticks = np.linspace(0, l - 1, 5)
xlabels = [str(i) + "?" for i in range(5)]
frames = 20
    
plt.clf()
plt.ylim(50, 70)
plt.xticks(xticks, xlabels)
plt.yticks([50, 60, 70])
plt.plotsize(100, 30)
plt.title("Streaming Data")
plt.colorless()

while True:
    tempList = []

    for j in range(10):
        tempList.append(getDecodedTemp())


    y = tempList

    for i in range(frames):
        
        plt.clp
        plt.cld()
        plt.clt()
        plt.scatter(x, y, marker = "dot")
        plt.sleep(0.05)
        plt.show()
