import re
import os
from time import sleep 
import string 
import RPi.GPIO as GPIO 
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

while True:
    tempraw = os.popen('vcgencmd measure_temp').readline()
    temp = int(re.search(r'\d+', tempraw).group())
    db.update({"CPU":temp})
    if temp>65:
        GPIO.output(Fanpin, True)
        db.update({"CPUFan":"ON"})
    else:
        GPIO.output(Fanpin, False)
        db.update({"CPUFan":"OFF"})
    Pump  = db.child("Pump").get().val()
    GPIO.output(Pumppin,Pump)
    Valve  = db.child("Valve").get().val()
    GPIO.output(Valvepin,Valve)
