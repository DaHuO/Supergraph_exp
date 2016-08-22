#!/usr/local/bin/python

from random import randint

def rTest(n, d, s):
	for i in range(0, 10):
		a = randint(2, n - 2)
		
		x = pow(a, d, n)
		if x == 1 or x == n - 1:
			continue
		
		test = False
		for k in range(s):
			x = pow(x, 2, n)
			if x == 1:
				return False
			if x == n - 1:
				test = True
				break
		if test:
			continue
		return False
	return True

def isComp(a, d, s, n):
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, (2**i) * d, n) == n - 1:
			return False
	return True

def test(n):
	for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
		if n % p == 0:
			return False
			
	if n == 2 or n == 3:
		return True
	d = n - 1
	i = 0
	while not d % 2:
		d = d >> 1
		i += 1

	if n < 1373653:
		return not any(isComp(a, d, i, n) for a in (2, 3))
	if n < 9080191:
		return not any(isComp(a, d, i, n) for a in (31, 73))
	if n < 4759123141:
		return not any(isComp(a, d, i, n) for a in (2, 7, 61))
	if n < 1122004669633:
		return not any(isComp(a, d, i, n) for a in (2, 13, 23, 1662803))
	if n < 2152302898747:
		return not any(isComp(a, d, i, n) for a in (2, 3, 5, 7, 11, 13))
	if n < 3474749660383:
		return not any(isComp(a, d, i, n) for a in (2, 3, 5, 7, 11, 13))
	if n < 341550071728321:
		return not any(isComp(a, d, i, n) for a in (2, 3, 5, 7, 11, 13, 17))
	return rTest(n, d, i)

j = 500

s = 10000000000000000000000000000000

def c(x):
  return [int(str(x), i) for i in xrange(2, 11)]

def nn(x):
  n = bin(int(str(x), 2) + int('1', 2))
  s = n[2:]

  while (s[0], s[len(s) - 1]) != ('1', '1'):
    n = bin(int(s, 2) + int('1', 2))
    s = n[2:]
  return int(s)

i = 0

a = []
while len(a) < j:
  s = nn(s)
  y = c(s)

  prime = False
  for x in y:
    if test(x):
      prime = True
      break

  if prime:
    continue

  aa = []
  for x in y:
    k = 2
    while True:
      if k > 50000:
        break
      if x % k == 0:
        aa.append(k)
        break
      k += 1
 
  if len(aa) == 9:
    a.append((s, aa))

with open('a.out', 'w') as f:
  f.write('Case #1:\n')
  for i in a:
    f.write(str(i[0])+ ' ')
    l = [str(y) for y in i[1]]
    l = ' '.join(l)
    f.write(l + '\n')

