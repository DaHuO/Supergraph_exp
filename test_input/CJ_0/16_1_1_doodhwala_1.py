for cases in range(1, int(input()) + 1):
	s = input()
	ans = s[0]
	for i in range(1,len(s)):
	    if(ord(s[i]) >= ord(ans[0])):
	        ans = s[i] + ans
	    else:
	        ans = ans + s[i]
	print('Case #%d:' % (cases,), ans)
