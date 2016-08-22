t = int(input())

for c in range(t):
	s = input()
	out = ""
	for ch in s:
		if ch >= out[:1]:
			out = ch + out
		else:
			out = out + ch
	print("Case #" + str(c + 1) + ": " + out)
