from sys import stdin

T = int(stdin.readline())

for t in range(T):
	letters = stdin.readline().strip()
	s = letters[0]

	for l in letters[1:]:
		if l >= s[0]:
			s = l + s
		else:
			s = s + l

	print("Case #{}: {}".format(t + 1, s))
