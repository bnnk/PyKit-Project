#!/usr/bin/env python3
########################################################################
# Filename    : Sweep.py
# Description : Servo sweep
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time
OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
servoPin = 12

def map( value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin's mode is output
    GPIO.output(servoPin, GPIO.LOW)  # Set servoPin to low

    p = GPIO.PWM(servoPin, 50)     # set Frequece to 50Hz
    p.start(0)                     # Duty Cycle = 0
    
def servoWrite(angle):      # make the servo rotate to specific angle (0-180 degrees) 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))#map the angle to duty cycle and output it

def rotate(dir):
    if (dir < 0):
        for dc in range(0, 31, 1):   #make servo rotate from 0 to 180 deg
            servoWrite(dc)     # Write to servo
            time.sleep(0.01)
    if (dir > 0):
        for dc in range(30, -1, -1): #make servo rotate from 180 to 0 deg
            servoWrite(dc)
            time.sleep(0.01)

def destroy():
    p.stop()
    GPIO.cleanup([servoPin])
