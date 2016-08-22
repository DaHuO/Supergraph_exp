t=input()
for i in range(1,t+1):
	s=raw_input()
	ans=[s[0]]
	c=ord(s[0])
	for j in range (1,len(s)):
		if ord(s[j])>=c:
			ans=[s[j]]+ans
			c=ord(s[j])
		else:
			ans.append(s[j])
	res="".join(ans)
	print "Case #"+str(i)+": "+res
