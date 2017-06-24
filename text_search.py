#Jason Jacobi
#Day 14 Assignment

findline = open('sample_text.txt')
count = 0
spam = 0
tot = 0
for line in findline:
	if 'X-DSPAM-Confidence:' in line:
		count = count + 1
		confidence = line.strip('X-DSPAM-Confidence:')
		tot= tot + float(confidence)
		average = str(tot/count)
		
		
print('There are %i lines with "X-DSPAM-Confidence:" in "sample_text.txt"' % (count))
print('The average spam confidence is %s') % (average)
