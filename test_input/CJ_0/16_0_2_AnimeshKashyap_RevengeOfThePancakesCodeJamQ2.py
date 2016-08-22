def invert(minusOrPlus):
	if minusOrPlus=='+':
		return '-'
	else:
		return '+'
T=int(raw_input())
for t in range(1,T+1):
	s=raw_input()
	sortedS=sorted(s)
	ans=0
	if(sortedS[0]==sortedS[len(sortedS)-1]):
		if(sortedS[0]=='+'):
			ans=0
		else:
			ans=1
	else:
		while sortedS[0]!=sortedS[len(sortedS)-1]:
			end=s.find(invert(s[0]));
			#print 'Before: '+s
			s=list(s)
			s[:end]=list(map(invert,s[:end]))
			ans+=1
			s=reduce(lambda x,y:x+y,s)
			#print 'After: '+s
			sortedS=sorted(s)
		if(sortedS[len(sortedS)-1]=='-'):
			ans+=1
	print 'Case #'+str(t)+': '+str(ans)