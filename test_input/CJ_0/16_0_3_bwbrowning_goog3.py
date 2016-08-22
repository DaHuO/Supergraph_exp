import sys
import time
import math

lines = sys.stdin.readlines()

inputs = lines[1].split(' ')

n = int(inputs[0])
j = int(inputs[1])

start = time.time()

def get_divisor(num):
	if num % 2 == 0:
		return 2
	for x in xrange(3, int(math.sqrt(num))+1, 2):
		#print 'trying %d mod %d' % (num, x)
		if time.time() - start > 4:
			return False
		if num % x == 0:
			return x
	return False

x = 2 ** (n-1) + 1
found = 0
print "Case #1:"
while True:
	start = time.time()
	if found == j:
		break
	binstr = "{0:b}".format(x)

	#print 'trying: %s' % binstr
	if len(binstr) > n:
		break

	divisors = []
	if binstr[0] == '1' and binstr[-1] == '1':
		# possible binstr
		for base in range(2,11):
			#print 'trying base: %d' % base
			#print 'trying base: %s , %d' % (binstr, base)
			div = get_divisor(int(binstr, base))
			divisors.append(div)
			if div is False:
				break
		if not( False in divisors):
			print binstr,
			for d in divisors:
				print d,
			print ""
			found = found + 1

	x = x + 1
