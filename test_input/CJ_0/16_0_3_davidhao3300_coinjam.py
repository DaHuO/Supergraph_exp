with open('coinjam.in') as f:
	data = f.read().split('\n')

def to_base(x, base):
	res = []
	divisor = base
	while divisor < x:
		divisor *= base
	divisor /= base
	while divisor > 0:
		res.append(x / divisor)
		x %= divisor
		divisor /= base
	return res

def convert_base(x, base):
	a = 0
	for i in range(len(x)):
		digit = x[len(x)-1-i]
		a += digit * base ** i
	return a

def is_prime(x, base):
	res = convert_base(x, base)
	#print res
	for i in range(2, int(res ** 0.5)+1):
		if res % i == 0:
			return i

with open('coinjam.out', 'w') as f:
	count = 0
	for i in range(1, len(data)):
		f.write('Case #{}:\n'.format(i))
		row = [int(x) for x in data[i].split(' ')]
		#print row
		n, j = row
		start = 2 ** (n - 1) + 1
		for x in range(start, 2 ** n, 2):
			base_two = to_base(x, 2)
			res = []
			for base in range(2, 11):
				proof = is_prime(base_two, base)
				if not proof:
					break
				else:
					res.append(proof)
			#print base_two, res
			if len(res) == 9:
				count += 1
				#print base_two, res
				f.write(''.join([str(x) for x in base_two]))
				f.write(' ')
				f.write(' '.join([str(x) for x in res]))
				f.write('\n')
				if count == j:
					break