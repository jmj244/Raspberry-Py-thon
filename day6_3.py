#Jason Jacobi

N = input ("Please enter a number as an upper limit:")
N = int (N)

print('The following numbers are the prime numbers below your chosen upper limit. Thank you.')

for i in range(2,N):
	check_var = True
	for k in range(2,i):
		if (i%k) == 0:
			check_var = False
	if check_var:
		print(i)
		
