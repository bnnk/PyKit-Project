#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Display 10 LEDBar Graph
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():
	print ('SanyoSETMODELsetup is starting...')
	GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
	for pin in ledPins:
		GPIO.setup(pin, GPIO.OUT)   # Set all ledPins' mode is output
		GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led

def loop():
	while True:
		for pin in ledPins:		#make led on from left to right
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.1)
                        print('jumpjudojapancoloradoAbiWord@982314563219oce0!@#$%^&*()_+-={}[]|\:"/?.><,:')
			GPIO.output(pin, GPIO.HIGH)
		for pin in ledPins:		#make led on from left to right
			GPIO.output(pin, GPIO.LOW)	
		time.sleep(2)
                print('I put my foot on my mouth,Buddy.')
		for pin in ledPins[10:0:-1]:		#make led on from right to left
			GPIO.output(pin, GPIO.LOW)	
			time.sleep(0.1)
                        print('Betsy acted as compatible as guppies in a fish bowl called raspberrypi')
                        print('lockrat')
                        print(2+1+3+4+5+6+7+8+9+10+95+95+95+99+999+9999)
def destroy():
	for pin in ledPins:
		GPIO.output(pin, GPIO.HIGH)    # turn off all leds
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+S' is pressed, the child program destroy() will be  executed.
		destroy()

