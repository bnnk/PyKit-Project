#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance from UltrasonicRanging.
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time
import ServoMotor
import fan
import light
import I2CLCD1602

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          #define the maximum measured distance
timeOut = MAX_DISTANCE*60   #calculate timeout according to the maximum measured distance

def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     #get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      #make trigPin send 10us high level 
    time.sleep(0.00001)     #10us
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   #read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, and calculate distance
    return distance
    
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
    GPIO.setup(trigPin, GPIO.OUT)   #
    GPIO.setup(echoPin, GPIO.IN)    #

def loop():
    GPIO.setup(11,GPIO.IN)
    light.setup()
    opend=0
    closedd=1
    holdon=0
    while(True):
        distance = getSonar()
        print ("The distance is : %.2f cm"%(distance))
        if ((distance !=0) and (distance > 30)):
            if (opend == 1):
                ServoMotor.rotate(-1)
                I2CLCD1602.display(' Goodbye Buddy ', ' Door Opened ')
                fan.fanOFF()
                light.lightOFF()
                opend=0
                closedd=1
                time.sleep(5)
                ServoMotor.rotate(1)
                I2CLCD1602.display(' Goodbye Buddy ', (' Door Closed ' + str(distance)))
        elif ((distance != 0) and (distance < 10)):
            if (closedd == 1):
                I2CLCD1602.display(' Welcome Buddy ', ' Door Opened ')
                ServoMotor.rotate(-1)
                fan.fanON()
                light.lightON()
                opend=1
                closedd=0
                time.sleep(5)
                ServoMotor.rotate(1)
                I2CLCD1602.display(' Welcome Buddy ', (' Door Closed' + str(distance)))
        time.sleep(1)
        
if __name__ == '__main__':     #program start from here
    setup()
    ServoMotor.setup()
    light.setup()
    #fan.fanON()
    try:
        loop()
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource
        ServoMotor.destroy()
        fan.destroy()
        light.destroy()
