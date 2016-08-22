#!/usr/bin/python


f = open('b.in')
l = int(f.readline())
for i in range(l):
	s = f.readline().strip()
	count = 0
	previous = ''
	for c in s:
		if not c == previous:
			previous = c
			count += 1
	numFlips = count-1 if s[-1]=='+' else count
	print 'Case #'+str(i+1)+": "+str(numFlips)
