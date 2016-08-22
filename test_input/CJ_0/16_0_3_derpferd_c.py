import cPickle as pickle
import sys

def put(s):
	sys.stdout.write(s)


print "Loading..."

# need to run c_pre to generate this list
primes = pickle.load(open("p.obj", "rb"))

raw_input("Ready for input. Press Any key to continue.")

print "Starting..."

sys.stdin = open("c.in", "r")
sys.stdout = open("c.out", "w")

raw_input()
N, J = map(int, raw_input().split())
# print >> sys.stderr, N,J

def isPrime2(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
		if n%i==0:
			return False    

	return True

def not_prime(n):
	# if n < 100000000 and n not in primes:
	# 	return True
	# try to figure it out
	for p in primes:
		if n%p == 0 and n!=p:
			return p
	return False

def get_comb(n):
	return "1" + bin(n)[2:].rjust(N-2, "0") + "1"

def test(s):
	# print "Trying", s
	ts = []
	for b in range(2, 11):
		n = int(s, b)
		t = not_prime(n)
		if not t:
			return False
		ts += [t]

	return ts

found = []

comb_i = 0

for i in range(J):
	cur = get_comb(comb_i)
	t = test(cur)
	while not t:
		comb_i += 1
		cur = get_comb(comb_i)
		t = test(cur)
	found.append((cur, t))
	comb_i += 1
	print >> sys.stderr, "Found", i

put("Case #1:\n")
for t in range(J):
	put(found[t][0] + " " + " ".join(map(str,found[t][1])) + "\n")
