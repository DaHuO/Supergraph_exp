for i in range(input()):
	print "Case #"+str(i+1)+":",
	a=raw_input()
	b=a[0]
	for j in xrange(1,len(a)):
		if a[j]!=b[0]:
			if a[j]>=b:
				b=a[j]+b
			else:
				b=b+a[j]
		else:
			b=a[j]+b

	print b