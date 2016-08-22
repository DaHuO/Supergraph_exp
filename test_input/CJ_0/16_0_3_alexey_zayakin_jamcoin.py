def check(x):
	f = []
	for b in range(2, 11):
		val = int(x, base = b)
		f += [0]
		for d in range(2, min(2 ** 16, val)):
			if val % d == 0:
				f[-1] = d
				break
	
	return f
				

n, k = map(int, input().split())

print('Case #1:')
for x in range(2 ** (n - 1) + 1, 2 ** n, 2):
	x = bin(x)[2:]
	f = check(x)
	if all(f):
		print(x, *f)
		k -= 1
		
		if k == 0: break
