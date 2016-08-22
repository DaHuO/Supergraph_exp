t = int(input())
for x in range(1, t+1):
	s=input()
	final=s[0]
	for y in range(1, len(s)):
		if(ord(s[y])<ord(final[0])):
			final = final+s[y]
		else:
			final = s[y]+final
	pri = "Case #"+str(x)+":"
	print(pri, final)

