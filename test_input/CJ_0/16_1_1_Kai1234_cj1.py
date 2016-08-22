t=int(input())
for i in range(1,t+1):
	s=input()
	j=[s[0]]
	for k in s[1:] :
		if(ord(k)>=ord(j[0])):
			j=[k]+j
		else:
			j.append(k)
	print('Case #'+str(i)+': '+''.join(j))