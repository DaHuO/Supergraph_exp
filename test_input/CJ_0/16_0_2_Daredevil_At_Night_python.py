a = int(raw_input())

for i in xrange(a):
	listI = list(raw_input())
	flips = 0
	if '-' not in listI:
		print ("Case #" + str(i+1)+": " + str(0))
	elif '+' not in listI:
		print ("Case #" + str(i+1)+": " + str(1))
	else:
		while '-' in listI:
			j = listI.index('-')
			if j == 0:					
				if '+' not in listI:
					print ("Case #" + str(i+1)+": " + str(flips+1))
					break
				j = listI.index('+')
				listI[:j] = list('+'*j)
				flips = flips + 1
			if '-' not in listI:
				print ("Case #" + str(i+1)+": " + str(flips))
				break
			j = listI.index('-')
			listI[:j] = list('-'*j)
			flips = flips + 1
