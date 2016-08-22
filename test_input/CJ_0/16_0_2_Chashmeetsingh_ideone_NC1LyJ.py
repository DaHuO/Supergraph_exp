t=input()
for z in range(t):
	n=raw_input()
	l = len(n)
	#print l
	ans=0
	
	if(n.count('+') == l):
		print "Case #%d: 0" % (z+1)
	else:
		i=0
		while(n.count('+') != l):
			ans+=1
			if(n[0] == '+'):
				cnt = 0
				for j in range(0,l):
					if(n[j] == '-'):
						break
					else:
						cnt += 1
				#print n
				for j in range(cnt):
					n = list(n) 
					n[j] = '-' 
					"".join(n)
				#print n
			else:
				cnt = 0
				for j in range(0,l):
					if(n[j] == '+'):
						break
					else:
						cnt += 1
				#print n
				for j in range(cnt):
					n = list(n) 
					n[j] = '+' 
					"".join(n)
				#print n
		print "Case #%d: %d" % (z+1,ans)