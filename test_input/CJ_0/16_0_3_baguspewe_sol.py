def is_prime(n):
	if n%2 == 0 or n%3 == 0:
		return False
	else:
		i = 5
		while i*i < n:
			if n%i == 0 or n%(i+2) == 0:
				return False
			i+=6
		return True

def non_trivial_divisor(n):
	if n%2 == 0:
		return 2
	elif n%3 == 0:
		return 3
	else:
		i = 5
		while i < 1000000: #i*i < n:
			if n%i == 0:
				return i
			elif n%(i+2) == 0:
				return i+2
			i+=6
		return 1

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
	[N, J] = [int(n) for n in raw_input().split(" ")]

	print "Case #1:"

	j = 0
	v = 0
	ntds = None
	while j < J:
		val = (1 << N-1) + (v << 1) + 1
		ntds = []
		base = {}

		coin_str = "{0:b}".format(val)
		coin = [int(i) for i in list(coin_str)]

		for x in xrange(2, 11):
			mult = 1
			base[x] = 0
			for y in xrange(1, N+1):
				base[x] += coin[-y]*mult
				mult *= x

			ntd = non_trivial_divisor(base[x])
			if (ntd > 1):
				ntds.append(ntd)
			else:
				break

		if len(ntds) == 9:
			j += 1
			print "%s %d %d %d %d %d %d %d %d %d" % (coin_str, ntds[0], ntds[1], ntds[2], ntds[3], ntds[4], ntds[5], ntds[6], ntds[7], ntds[8])
		v += 1
