def solve(ip):

	count = 0
	ip = list(ip)

	for i in range(0,len(ip)-1):
		
		if ip[i] != ip[i+1]:

			for j in range(0,i+1):
				ip[j] = ip[i+1]

			count = count + 1

	if ip[0] == '-':
		count = count + 1 		


	return count	



t = int(raw_input())

for i in xrange(1, t + 1):
	val = solve(raw_input()) 
	print "Case #{}: {}".format(i,val)
