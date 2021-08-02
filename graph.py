#live graph of core temperature

import plotext as plt
import numpy as np
import subprocess as sub


bash = ["/opt/vc/bin/vcgencmd", "measure_temp"]

process = sub.Popen(bash, stdout=sub.PIPE)

output, error = process.communicate()

print(output)

exit()
