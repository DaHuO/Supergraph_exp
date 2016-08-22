import sys
import math

def check(bin):
	strnum = ""
	tmp = bin
	divisors = []
	while tmp > 0:
		strnum = str(tmp%2) + strnum
		tmp /= 2
	for base in xrange(2, 11):
		x = int(strnum, base)
		# print x
		isp = isprime(x)
		if isp == True:
			return False
		divisors.append(isp)
	return (strnum, divisors)



def isprime(num):
	max_check = int(math.floor(math.sqrt(num)))

	for i in xrange(2, max_check+1):
		if num % i == 0:
			return i

	return True

lines = sys.stdin.readlines()
lines = map(str.strip, lines)

T = int(lines[0])

N, J = map(int, lines[1].split())

print "Case #1:"

start = 2**(N-1)

tot = 0
while tot < J:
	if start%2 == 0:
		start += 1
		continue
	ch = check(start)
	if ch == False:
		start += 1
		continue
	strnum, divisors = ch
	print strnum + " " + ' '.join(map(str,divisors))
	tot += 1
	start += 1