import random

raw_input()

def generate(k):
	res = []
	for i in xrange(k-2):
		res.append(str(random.randint(0,1)))
	return ["1"]+res+["1"]

def divisor(k):
	i = 2
	while i < 5000 and i*i <= k:
		if k%i == 0:
			return i
		i += 1
	return -1

n, j = map(int, raw_input().split())
seen = set()
print "Case #1:"
count = 0
while count < j:
	please = "".join(generate(n))
	if please not in seen:
		ok = True
		res = []
		for b in xrange(2, 11):
			r = divisor(int(please, b))
			if r == -1:
				ok = False
			else:
				res.append(str(r))

		if ok:
			count += 1
			print please, " ".join(res)
	seen.add(please)