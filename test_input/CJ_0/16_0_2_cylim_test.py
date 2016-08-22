def flip(pencake, number):
	pencake[0:number:-1]
	for i in range(number):
		if pencake[i] == '-':
			pencake[i] = '+'
		else:
			pencake[i] = '-'


t = int(input())
for i in range(1, t + 1):
	pencake = list(input())

	count = 0
	while "-" in pencake:
		for num in reversed(range(len(pencake))):
			if pencake[num] == "-":
				flip(pencake, num+1)
				count += 1
			
	if not "-" in pencake:
		print("Case #{}: {}".format(i, count))
