T = int(input())

for i in range(T):
	word = input()
	s = word[0]
	for c in word[1:]:
		if ord(c) >= ord(s[0]):
			s = c + s
		else:
			s = s + c
	print("Case #{}: {}".format(i + 1, s))