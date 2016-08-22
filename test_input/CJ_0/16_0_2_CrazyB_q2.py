
def change(var):
	if(var=='+'):
		return '-'
	else:
		return '+'

t=int(raw_input())
for i in xrange(t):
	l=raw_input()
	l=l[::-1]
	var='+'
	count=0
	for j in xrange(len(l)):
		if(l[j]!=var):
			count=count +1
			var=change(var)
	print "Case #"+str(i+1)+": "+str(count)


