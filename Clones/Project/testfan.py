#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

#GPIO-5
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setwarnings(False)

def fanOFF():
    destroy()
    return()

def fanON():
    setup()
    setPin(True)
    return()

def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(29, mode)
    return()

def destroy():
    GPIO.cleanup([29])
    return()

if __name__ == '__main__':     #program start from here
    while(True):
        fanON()
        sleep(5)
        fanOFF()
        sleep(5)
