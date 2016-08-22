T=int(raw_input())
t=1
while t<=T:
	S=raw_input()
	l=len(S)
	srtdS=sorted(S)
	i=0
	ans=''
	while i<l:
		# print '****'
		# print ans
		# print i
		# print '****'
		if(i==0):
			ans+=S[i]
			i+=1
		else:
			if(S[i]>=ans[0]):
				ans=S[i]+ans
				i+=1
			else:
				ans=ans+S[i]
				i+=1
	print 'Case #'+str(t)+': '+ans
	t+=1