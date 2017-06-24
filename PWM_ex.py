import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_num = 18
GPIO.setup(pin_num,GPIO.OUT)

pwm_led = GPIO.PWM(pin_num,500)
pwm_led.start(100)

try:
	while True:
		duty_s = input("Please enter the duty cycle of PWM (LED brightness):")
		duty = int(duty_s)
		pwm_led.ChangeDutyCycle(duty)
		
finally:
	print("cleaning up")
	GPIO.cleanup()
