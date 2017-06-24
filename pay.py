#Jason Jacobi

hours = input('How many hours did you work?')
rate = input('What is your hourly rate?')
gross_pay= rate*hours

if hours>40:
	print('Your total pay is: $' +str(gross_pay*1.5))

else:
	print('Your total pay is: $' +str(gross_pay))
	

