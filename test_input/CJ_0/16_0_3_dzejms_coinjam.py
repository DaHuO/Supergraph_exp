from itertools import product
from random import random
import signal

class AlarmException(Exception):
	pass

def alarmHandler(signum, frame):
	raise AlarmException

def get_divisor(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return i
		i += 1
	return False

def get_jamcoin(n):
	for inner in product('01', repeat=n-2):
		yield ('1',) + inner + ('1',)

def get_jamcoin2(count, seen):
	while True:
		num = ''.join([str(int(random() < 0.5)) for x in range(count)])
		if num not in seen:
			seen.add(num)
			return "{}{}{}".format(1, num, 1)

'''
nums = get_jamcoin(n)

for _ in range(n):
	print(nums.next())
'''

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	n, c = [int(s) for s in input().split(" ")] 

	print("Case #{}: ".format(i))
	seen = set()
	coin_jams = []
	while len(coin_jams) != c:
		num = get_jamcoin2(n-2, seen)
		divs = []

		for base in range(2, 11):
			new_base = int(num, base)
			signal.signal(signal.SIGALRM, alarmHandler)
			signal.setitimer(signal.ITIMER_REAL, 0.1)
			try:
				div = get_divisor(new_base)
				signal.alarm(0)
			except AlarmException:
				#print("too long")
				break
			if div == False:
				break
			#print(base, new_base, div)
			divs.append(str(div))

		if len(divs) != 9:
			continue

		print(num, ' '.join(divs))
		coin_jams.append(num)



