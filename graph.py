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

#print(output)
#print(ftemp)

tempList = []

for x in range(5):
    tempList.append(decodeTemp(getTemp()))

plt.scatter(tempList)
plt.plotsize(50,30)
plt.title("Temperatura")
plt.show()

#marker = dot
#color = artic / teal / basil

exit()
