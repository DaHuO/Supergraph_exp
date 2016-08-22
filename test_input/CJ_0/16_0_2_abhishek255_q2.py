def flip(x):
	x.reverse()
	for d in range(len(x)):
		if x[d]=='-':
			x[d]='+'
		else:
			x[d]='-'
	return x

def cnt(q):
	count=0
	if q[0]=='-':
		while '-' in q:
			if '+' in q:
				index=q.index('+')
				q[:index]=flip(q[:index])
				count+=1
				#print "q for 1 of 1: ",q
			else:
				count+=1
				break
			if '-' in q:
				index=q.index('-')
				q[:index]=flip(q[:index])
				count+=1
				#print "q for 2 of 1: ",q
		#else:
		#	break
	else:
		while '-' in q:
			if '-' in q:
				index=q.index('-')
				q[:index]=flip(q[:index])
				count+=1
				#print "q for 1 of 1: ",q
			if '+' in q:
				index=q.index('+')
				q[:index]=flip(q[:index])
				count+=1
				#print "q for 2 of 1: ",q
			else:
				count+=1
				#print "only - left"
				return count		#else:
		#	break
	return count


#def counting(x):
#	count=0
#	while '+' in x:
#		index=x.index('+')
#		count+=1
#		while x[index]=='+':
#			x.remove(x[index])
#	return count

for a in range(input()):
	q=list(raw_input())
	print "Case #"+str(a+1)+":",
	print cnt(q)
	
