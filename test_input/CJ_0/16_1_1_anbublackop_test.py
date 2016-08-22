for _ in range(int(input())):
	s=input()
	s2=s[0]
	for i in range(1,len(s)):
		if ord(s[i])>=ord(s2[0]):
			s2=s[i]+s2
		else:
			s2=s2+s[i]
	print ("Case #{}: {}".format(_+1,s2))	
