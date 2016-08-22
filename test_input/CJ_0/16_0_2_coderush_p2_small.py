t=int(raw_input())
for tcase in xrange(t):
	pcakes=raw_input().strip()
	flips=0
	for i in xrange(len(pcakes)-1):
		if pcakes[i]!=pcakes[i+1]:
			flips+=1
	if pcakes[-1]=='-':
		flips+=1
	print "Case #"+str(tcase+1)+": "+str(flips)

