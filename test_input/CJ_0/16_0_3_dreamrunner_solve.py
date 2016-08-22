def is_prime(n):
	"""check if integer n is a prime"""
	# make sure n is a positive integer

	n = abs(int(n))  # 0 and 1 are not primes
	if n < 2:
		return False

	# 2 is the only even prime number
	if n == 2:
		return True

		# all other even numbers are not primes
	if not n & 1:
		return False

	# range starts with 3 and only needs to go up
	# the square root of n for all odd numbers
	for x in range(3, int(n ** 0.5) + 1, 2):
		if n % x == 0:
			return False

	return True


def to_binary(n):
	s = ""
	while n > 0:
		if n % 2:
			s = "1" + s
		else:
			s = "0" + s
		n //= 2
	return s


def to_base(val, base):
	output = 0
	for c in val:
		output *= base
		if c == "1":
			output += 1
	return output


def get_divisor(val):
	for i in range(2, val - 1):
		if val % i == 0:
			return i


def test(val):
	if val[-1] == "0":
		return False
	is_ok = True
	for base in range(2, 11):
		val_in_base = to_base(val, base)
		# print(val, base, val_in_base)
		if is_prime(val_in_base):
			is_ok = False
	if is_ok:
		print(val, end="")
		for base in range(2, 11):
			print(" " + str(get_divisor(to_base(val, base))), end="")
		print()
		return True
	return False


def solve(n, j):
	val = 2**(n-1)
	found = 0
	while found < j:
		# print("test=" + to_binary(val))
		if test(to_binary(val)):
			found += 1
		val += 1


def main():
	num_of_test = int(input())

	for test_id in range(1, num_of_test + 1):
		n, j = (int(i) for i in input().split())
		print("Case #" + str(test_id) + ":")
		solve(n, j)

if __name__ == "__main__":
	main()