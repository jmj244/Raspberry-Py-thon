#Jason Jacobi
#HW1.d

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

integer = 0
integer = input('Please choose an integer between 1 and 3:')

if integer == 1:
	GPIO.output(17,1)
	time.sleep(1)

elif integer == 2:
	GPIO.output(17,1)
	GPIO.output(18,1)
	time.sleep(1)

elif integer == 3:
	GPIO.output(17,1)
	GPIO.output(18,1)
	GPIO.output(27,1)
	GPIO.output(22,1)
	time.sleep(1)

else:
	print ('ERROR: You did not follow the directions. Good-bye')

GPIO.output(17,0)
GPIO.output(18,0)
GPIO.output(27,0)
GPIO.output(22,0)

GPIO.cleanup()


