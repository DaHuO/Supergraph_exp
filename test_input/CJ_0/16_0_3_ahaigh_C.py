import sys
import itertools

def getdiv(x):
	t = 2
	while t*t <= x and t < 50:
		if (x % t == 0):
			return t
		t = t + 1
	return None

def test(n, j):
	a = []
	for z in itertools.product(*([0, 1] for i in xrange(0, n))):
		z = (1,) + z + (1,)
		def val(z, base):
			sum = 0
			for i in xrange(0, len(z)):
				sum = base*sum + z[i]
			return sum

		v = [val(z, b) for b in xrange(2,11)]
		d = [getdiv(x) for x in v]
		if None not in d:
			print ''.join(str(x) for x in z), ' '.join(str(x) for x in d)
			a = a + [z]
			if len(a) >= j:
				return a
#		print z

def main():
	s = sys.stdin.readline()
	T = int(s)
	s = sys.stdin.readline()
	n, j = (int(x) for x in s.split())
#	print n, j

	print "Case #1:"
	test(n-2, j)

if __name__ == "__main__":
	main()
