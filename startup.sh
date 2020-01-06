#!/bin/sh
SERVICE_DATA='python3 /home/pi/blrdemo/data.py'
SERVICE_PINS='python3 /home/pi/blrdemo/pins.py'
SERVICE_FAN='python3 /home/pi/blrdemo/fan.py'

if ps ax | grep -v grep | grep $SERVICE_DATA > /dev/null
then
    echo "Sensor script already running"
else
    echo "Sensor is not running, starting..."
    sudo $SERVICE_DATA > /dev/null &
    echo "Sensor collecting script started"
fi

if ps ax | grep -v grep | grep $SERVICE_PINS > /dev/null
then
    echo "Commands script already running"
else
    echo "Commands script is not running, starting..."
    sudo $SERVICE_PINS > /dev/null &
    echo "Commands script started"
fi

if ps ax | grep -v grep | grep $SERVICE_FAN > /dev/null
then
    echo "fan script already running"
else
    echo "Fan is not running, starting..."
    sudo $SERVICE_FAN > /dev/null &
    echo "Fan script started"
