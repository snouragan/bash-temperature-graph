#live graph of core temperature

import plotext as plt
import numpy as np
import subprocess as sub

bash = ["/opt/vc/bin/vcgencmd", "measure_temp"]

process = sub.Popen(bash, stdout=sub.PIPE)
output, error = process.communicate()

temp = output[5:9]
temp = temp.decode()
ftemp = float(temp)

#print(output)
print(ftemp)

#marker = dot
#color = artic / teal / basil

exit()
