#Jason Jacobi
#Day 7 Assignment

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_num = 18
GPIO.setup(pin_num,GPIO.OUT)

pwm_led = GPIO.PWM(pin_num,500)
dc=50
pwm_led.start(dc)

pin_num = 23
GPIO.setup(pin_num,GPIO.IN,pull_up_down=GPIO.PUD_UP)

pin_num2 = 26
GPIO.setup(pin_num2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	
try:
	while True:
		0<dc<100
		if GPIO.input(pin_num) == 0:
			pwm_led.ChangeDutyCycle(dc)
			print('LED Brightness increased by 5%')
			if dc<100:
				dc=dc+5
			time.sleep(.25)
			dc<100
		
			#time.sleep(1)
			
		if GPIO.input(pin_num2) == 0:
			pwm_led.ChangeDutyCycle(dc)
			print('LED Brightness decreased by 5%')
			if dc>0:
				dc=dc-5
			time.sleep(.25)
			dc>1
		
finally:
	print("cleaning up")
GPIO.cleanup()
