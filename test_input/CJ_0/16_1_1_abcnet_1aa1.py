import sys

f = open(sys.argv[1], 'r')
result = open(sys.argv[1]+'.sol','w')
T=eval(f.readline())



print 'T = ', T
for t in range(T):
	print "Case #", t+1
	S=f.readline()[:-1]
	print S
	r = S[0]
	for s in S[1:]:
		if s>=r[0]:
			r=s+r
		else:
			r=r+s
	result.write('Case #'+str(t+1)+': '+r+'\n')


f.close()
result.close()