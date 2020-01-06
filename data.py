import pyrebase
import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
from time import sleep

config = {
  "apiKey": "AIzaSyBrSQ_XMS9_zNgQ-Qv40TcuKLpOK_1Tbl4",
  "authDomain": "switch-e7401.firebaseapp.com",
  "databaseURL": "https://switch-e7401.firebaseio.com",
  "storageBucket": "switch-e7401.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    Data_set = db.child("Bool").get().val()
    print (Data_set)
    if (Data_set=="set"):
        print ("condition met")
        db.update({"Bool":"reset"})
        ser.write(b'data')
        sleep(2)
        if(ser.in_waiting>0):
            line = ser.readline().decode("utf-8")
            print (line)
            db.update({"Data":line})