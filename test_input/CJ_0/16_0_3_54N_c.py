#!/usr/bin/python

luts = []

def initlut():
	for i in range(2,11):
		l = []
		for k in range(0,32):
			l.append(i**k)
		luts.append(l)

# stackoverflow
def is_prime(n):
  if n == 2 or n == 3: return True, 0
	# never happens in our case?
  if n < 2: return False, 1
  if n%2 == 0: return False, 2
  if n < 9: return True, 0
  if n%3 == 0: return False, 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False, f
    if n%(f+2) == 0: return False, f+2
    f +=6
  return True, 0

def is_prime_nt(n):
	x, y = is_prime(n)
	return y

def yield_coin(N):
	hbit = 2**(N-1)
	for i in range(0,2**(N-2)):
		s = "{0:b}".format(hbit + i*2 + 1)
		bits = [int(x) for x in reversed(s)]
		nums = []
		for lut in luts:
			nums.append(sum([y for x,y in zip(bits,lut) if x==1]))

		divisor = []
		for x in nums:
			y = is_prime_nt(x)
			divisor.append(y)
			if y == 0:
				break

		if all(divisor):
			yield s, nums, divisor

initlut()

N = 16
J = 50
print "Case #1:"

case = 0
for s, nums, divisor in yield_coin(N):
	print s, " ".join([str(x) for x in divisor])
	case += 1
	#print case, s, nums, divisor
	if case == J:
		break
