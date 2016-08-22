def problem2Helper(s):
	prev = s[0]
	count = 1
	for i in s[1:]:
		if i != prev:
			prev = i
			count += 1
	if prev == '+':
		count -= 1
	return count


def problem2():
	data = []
	with open("Problem2Input.txt","r") as file:
		for lines in file:
			if lines[-1] == '\n':
				lines = lines[:-1]
			data += [lines]

	loop = int(data[0])

	for i in range(1,loop+1):
		print "Case #" + str(i) + ": " + str(problem2Helper(data[i]))


problem2()
