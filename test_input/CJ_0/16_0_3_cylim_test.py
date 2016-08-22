def check(digit):
	digit[0] = 1
	digit[len(digit) - 1] = 1

	answer = []
	answer.append(digit)
	for i in range(2, 11):
		num = toDecimal(digit, i)
		prime = isNotPrime(num)
		if prime:
			answer.append(prime)
		else:
			return False
	return answer

def show(answer):
	print(*answer[0], sep='', end=' ')
	print(*answer[1:len(answer)], sep=' ')

def isNotPrime(n):
	if n == 2:
		return False
	if n % 2 == 0:
		return 2

	sqr = int(pow(n, 0.5)) + 1
	for divisor in range(3, 1000, 2):
		if n % divisor == 0:
			return divisor

	return False

def toDecimal(number, base):
	num = 0
	number = number[::-1]
	for i in range(len(number)):
		num += number[i]*pow(base, i)
	return num

t = int(input())
for i in range(1, t + 1):
	n, j = [int(s) for s in input().split(" ")]

	print("Case #{}:".format(i))
	digit = [0 for i in range(n)]
	
	count = 0

	answer = check(digit)
	if answer != False:
		count += 1
		show(answer)

	while 0 in digit:
		number = int(''.join([ "%d"%x for x in digit]), 2) + 2
		number = int(bin(number)[2:])

		digit = list(map(int,str(number)))
		answer = check(digit)
		if answer != False:
			count += 1
			show(answer)

		if count == j:
			break;

