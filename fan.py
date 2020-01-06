import re
import os
import time
import logging

temp2 = os.popen('vcgencmd measure_temp').readline()
temp = int(re.search(r'\d+', temp2).group())


while True:
  try:
    if temp>40:
        print("HIGH")
    else:
        print("LOW")
    print(temp)
    time.sleep(1)
  catch Exception as e:
    logging.error("error occurred in fan.py : " + str(e))