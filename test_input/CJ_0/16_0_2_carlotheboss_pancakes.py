for i in range(int(input())):
	S=input()
	c= (S[0]=='-')
	print("Case #%s: %s" %(i+1, c+2 * (len([k for k in S.split('+') if len(k)>0]) - c)))
	
