import random

def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    cnt = 0

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

        cnt += 1
        if cnt == 10000:
        	return True

    return True

def get_divisor(n):
	i = 1
	while True:
		i += 1
		if n % i == 0:
			return i



def string_gen(n):
	middle = 0
	m = 2**(n-2) - 1

	while True:
		middle = random.randint(0, 2**(n-2) - 1)
		b = bin(middle)[2:]
		l = len(b)
		yield "1" + (n - 2 - l)*"0" + b + "1"

def isjamcoin(s):
	return not any(isprime(int(s, b)) for b in range(2,11))


if __name__ == "__main__":
	t = input()

	n, j = map(int, raw_input().split())

	print "Case #1:"
	count = 0
	coins = set()
	for g in string_gen(n):
		if isjamcoin(g) and g not in coins:
			coins.add(g)
			count += 1
			print g, " ".join(str(get_divisor(int(g, b))) for b in range(2,11))
			if count == j:
				break