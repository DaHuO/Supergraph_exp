T = int(raw_input())
for i in xrange(T):
	l = raw_input()
	ind = 1
	sign = l[0]
	cost = 0
	while ind < len(l):
		if l[ind] == sign:
			ind+=1
		else:
			sign = l[ind]
			cost+=1
			ind+=1
	if l[-1] == '+':
		print "Case #%d: %d" %(i+1,cost) 
	else:
		print "Case #%d: %d" %(i+1,cost+1) 
	
