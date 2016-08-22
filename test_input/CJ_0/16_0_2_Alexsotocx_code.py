
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	s = input()
	total = 0
	for j in range(len(s) - 1):
		if s[j] != s[j+1]:
			total += 1
	if s[len(s)-1] == '-':
		total += 1
	print("Case #{}: {}".format(i, total))


	# check out .format's specification for more formatting options