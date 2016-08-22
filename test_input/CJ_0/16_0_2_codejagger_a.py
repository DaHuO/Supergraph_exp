import re

t = raw_input()
t = int(t)
cc = 1
while t != 0:
	string = raw_input()
	string = re.sub('-+', '-', string)
	ans = 0
	for i, c in enumerate(string):
		if i == 0 and c == '-':
			ans += 1
		elif c == '-':
			ans += 2
	print("Case #{0}: {1}".format(cc, ans))
	cc += 1
	t -= 1
