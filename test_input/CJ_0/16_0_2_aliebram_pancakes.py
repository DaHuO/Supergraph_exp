def rec(word):
	e=0
	l=word[0]
	c=word[0]
	for c in word:
		if(c!=l):
			e+=1
		l=c
	if(c=='-'):
		e+=1
	return e
fi = open('in_large_pancakes', 'r')
fo = open('out','w')
n=int(fi.readline().split()[0])
for x in range(1,n+1):
	curr=fi.readline().split()[0]
	fo.write("Case #{}: {}\n".format(x,rec(curr)))

