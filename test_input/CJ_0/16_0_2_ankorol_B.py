N = int(input())
for t in range(1, N + 1):
	s = input()
	ans = 0
	for i in reversed(s):
		if (ans % 2 == 0 and i == '-') or (ans % 2 == 1 and i == '+'):
			ans += 1
	print("Case #{0}: {1}".format(t, ans))
