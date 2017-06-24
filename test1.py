#Jason Jacobi
#Test 1.5

x = input('Please enter a number')
x=int(x)
mylist= input('Please enter a list of coefficients from highest to lowest')

for i in mylist:
	total = mylist*x**mylist
	
print('The total value is', total)
