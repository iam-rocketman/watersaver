import re
import os
from time import sleep 
import string 
import RPi.GPIO as GPIO 
import logging

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
Valvepin = 21 
Pumppin = 20 
Fanpin = 16
GPIO.setup(Valvepin,GPIO.OUT) 
GPIO.setup(Pumppin,GPIO.OUT)
GPIO.setup(Fanpin,GPIO.OUT)

import pyrebase

config = {
  "apiKey": "AIzaSyBrSQ_XMS9_zNgQ-Qv40TcuKLpOK_1Tbl4",
  "authDomain": "switch-e7401.firebaseapp.com",
  "databaseURL": "https://switch-e7401.firebaseio.com",
  "storageBucket": "switch-e7401.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#db.child("users").child("Morty")

prevPump = None
prevValve = None

def makeDBCall(data):
  try:
    db.update(data)
  except Exception as e:
    logging.error("error encountered: "+ str(e))

while True:
    try:
      tempraw = os.popen('vcgencmd measure_temp').readline()
      temp = int(re.search(r'\d+', tempraw).group())
      makeDBCall({"CPU":temp})
      if temp>65:
          GPIO.output(Fanpin, True)
          makeDBCall({"CPUFan":"ON"})
      else:
          GPIO.output(Fanpin, False)
          makeDBCall({"CPUFan":"OFF"})
      try:
        Pump  = db.child("Pump").get().val()
        if prevPump != Pump:
          GPIO.output(Pumppin,Pump)
          prevPump = Pump
      catch Exception as e:
        logging.error("error in getting db child pump value: " + str(e))
      try:
        Valve  = db.child("Valve").get().val()
        if prevValve != Valve:
          GPIO.output(Valvepin,Valve)
          prevValve = Valve
      catch Exception as e:
        logging.error("error in getting db child valve value: " + str(e))
    catch Exception as e:
      logging.error(e)
      