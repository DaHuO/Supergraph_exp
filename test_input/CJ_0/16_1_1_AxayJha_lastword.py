t=int(input())
for t0 in range(t):
	s=str(input())
	lw=s[0]

	for i in range(1, len(s)):
		if s[i]>=lw[0]: lw=s[i]+lw
		else: lw=lw+s[i]

	print("Case #" + str(t0+1) + ": "+ lw)	