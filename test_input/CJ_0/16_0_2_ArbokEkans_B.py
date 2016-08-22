def f(s):
	if not s: return 0
	ans = 0
	for pos in range(len(s)-1): ans += s[pos] != s[pos+1]
	ans += s[-1] == '-'
	return ans

#for i in range(1, 10**6):
#	if f(i)//i >= 30:
#		print(i, f(i)//i)

for case in range(int(input())):
	print('Case #{}: {}'.format(case+1, f(input())))