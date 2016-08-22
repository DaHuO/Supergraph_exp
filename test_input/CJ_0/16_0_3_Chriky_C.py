import codejam as gcj
gcj.load_input('C-large.in')

T = gcj.read_input('i')
for t in range(T):
	N, J = gcj.read_input('i i')

	print 'Case #%i:' % (t + 1)

	for n in xrange(2**N):
		coin = '1%s1' % bin(n)[2:].zfill(N - 2)

		divisors = []
		for base in range(9):
			value = int(coin, base + 2)
			for p in [2, 3, 5, 7, 11]:
				if value % p == 0:
					divisors += [p]
					break
			else:
				break
		else:
			print coin, ' '.join(map(str, divisors))
			J -= 1

		if J == 0:
			break
