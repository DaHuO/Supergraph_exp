import itertools


def is_prime(n):
	if n == 2 or n == 3:
		return -1
	if n < 2 or n % 2 == 0:
		return 2
	if n < 9:
		return -1
	if n % 3 == 0:
		return 3
	r = 10000
	div = 5
	while div <= r:
		if n % div == 0:
			return div
		if n % (div + 2) == 0:
			return div + 2
		div += 6
	return -1



fr = open('/home/rafail/Desktop/code_jam/input3.in', 'r')
fw = open ('/home/rafail/Desktop/code_jam/output3.out', 'w')

t=fr.readline().rstrip()
t = int(t)

for i in range(1, t + 1):
	inp = fr.readline().split()
	iterator = itertools.count()
	count = 0
	fw.write("Case #" + str(i)+":\n")
	for num in iterator:
		fnum = "%030d" % (int(bin(num)[2:]),)
		fnum = '1{0}1'.format(fnum)
		divisors = []
		for base in range(2, 11):
			suma = 0
			base2 = 1
			for index in range(-1, -(int(inp[0]) + 1), -1):
				suma += int(fnum[index]) * base2
				base2 *= base
			q= is_prime(suma)
			if q > 0:
				divisors.append(q)
			else:
				break
		if (len(divisors)) == 9:
			fw.write("{0} {1}\n".format(fnum, " ".join(map(str, divisors))))
			count += 1
		if count == int(inp[1]):
			break 
			
fw.close()
fr.close()			
