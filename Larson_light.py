#Jason Jacobi
#Day 7 Assignment

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [4,17,18,27]
pins2 = [27,18,17,4]

try:
	while True:
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin,1)
			time.sleep(.5)
			GPIO.output(pin,0)
		time.sleep(.25)
	
		for pin in pins2:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin,1)
			time.sleep(.5)
			GPIO.output(pin,0)
		time.sleep(.25)

finally:
	for pin in pins:
		GPIO.output(pin,0)
	print("cleaning up")
GPIO.cleanup()
