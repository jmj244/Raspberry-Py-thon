quantity = range(0,10)
total = range(50,56)
for nuggets in total:
	for a in quantity:
		for b in quantity:
			for c in quantity:
				if nuggets == 6*a + 9*b +20*c:
					print a, 'six-packs,', b, 'nine-packs,', c, 'twenty-packs,', 'equals', nuggets, 'nuggets'
