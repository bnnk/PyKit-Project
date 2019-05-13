import RPi.GPIO as GPIO
led=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
