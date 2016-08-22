f = open('B-small-attempt0.in', 'r')
o = open('B-small-attempt0.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
	count = 0
	firstelement = 0
	lastchar = '0'
	originalstr = f.readline().strip()
	chararray = list(originalstr)
	for char in reversed(chararray):
		if(firstelement == 0):
			if(char == '-'):
				count += 1
			firstelement = 1
		else:
			if(char != lastchar ):
				count += 1
		lastchar = char
	# print count

	s = "Case #%d: %s\n" % (t+1, count)
	o.write(s)
	print s
	
print "This line will be printed."

