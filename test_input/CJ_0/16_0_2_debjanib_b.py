def solve(str):
	L = len(str)

	if "+"*L == str:
		return 0
	
	N = L

	for i in range(L-1):
		if s[i] == s[i+1]:
			N-=1
	if s[-1] == "+":
		N-=1
	return N

T = int(raw_input())
for t in range(T):
	s =raw_input()
	print ("Case #%d: %d" % (t+1, solve(s)))