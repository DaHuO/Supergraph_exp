n = 32
k = 500
cur = (1 << (n - 1)) + 1
print('Case #1:')
while k:
	divisors = []
	for i in range(2, 11):
		for j in range(2, 200):
			if int(bin(cur)[2:], i) % j == 0:
				divisors.append(j)
				break
	if len(divisors) == 9:
		k -= 1
		print(bin(cur)[2:], end = ' ')
		for j in divisors:
			print(j, end = ' ')
		print()
	if len(bin(cur)) - 2 > n:
		break
	cur += 2