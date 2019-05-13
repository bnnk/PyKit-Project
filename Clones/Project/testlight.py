#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setwarnings(False)

def lightOFF():
    setPin(False)
    return()

def lightON():
    setPin(True)
    return()

def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(31, mode)
    return()

if __name__ == '__main__':     #program start from here
    setup()
    try:
        while(True):
            lightON()
            sleep(5)
            lightOFF()
            sleep(5)
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource
