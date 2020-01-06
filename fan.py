import re
import os
import time

temp2 = os.popen('vcgencmd measure_temp').readline()
temp = int(re.search(r'\d+', temp2).group())


while True:
        if temp>40:
            print("HIGH")
        else:
            print("LOW")
        print(temp)
        time.sleep(1)