#!/usr/bin/env python3
########################################################################
# Filename    : BreathingLED.py
# Description : A breathing LED
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time

LedPin = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

p=[]
def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	for pin in LedPin:
	    GPIO.setup(pin, GPIO.OUT)   # Set LedPin's mode is output
	    GPIO.output(pin, GPIO.LOW)  # Set LedPin to low

	for pin in LedPin:
            pp=GPIO.PWM(pin, 1000)
	    p.append(pp)     # set Frequece to 1KHz
	    p[len(p)-1].start(0)              # Duty Cycle = 0

def loop():
	while True:
		for dc in range(0, 101, 1):   # Increase duty cycle: 0~100
                    for pin in p:
			pin.ChangeDutyCycle(dc)     # Change duty cycle
		    time.sleep(0.01)
		time.sleep(1)
		for dc in range(100, -1, -1): # Decrease duty cycle: 100~0
                    for pin in p:
			pin.ChangeDutyCycle(dc)
		    time.sleep(0.01)
		time.sleep(1)

def destroy():
        for pin in p:
	    pin.stop()
	for pin in LedPin:
	    GPIO.output(pin, GPIO.LOW)    # turn off led
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
