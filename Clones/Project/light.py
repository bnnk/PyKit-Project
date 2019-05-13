#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

#GPIO-6

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

def destroy():
    GPIO.cleanup([31])
    return()
