raw_input()
N,J= map(int,raw_input().split(' '))
lim = N/2-2
print "Case #1:"
for i in xrange(2**lim):
	s = str(bin(i))[2:]
	s = "1" + "0"*(lim-len(s))+s + "1"
	print s+s,
	for base in xrange(2,11):
		print base**(N/2)+1,
	print ""
	J-=1
	if J==0:
		break

