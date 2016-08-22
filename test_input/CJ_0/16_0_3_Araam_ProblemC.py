from math import sqrt


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def get_smallest_divisor(x):
	i = 2
	while i < sqrt(x):
		if x % i == 0:
			return i
		i += 1

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		with open('output.txt', 'w') as o:
			lines_list = f.read().splitlines()[1:]
			for idx, lines in enumerate(lines_list):
				o.write("Case #{}:\n".format(idx + 1))
				solutions = []
				size, cases = map(int, lines.split())
				count = 0
				num = [0] * size
				num[0] = 1
				num[-1] = 1
				val = int(''.join(str(c) for c in num), 2)
				max_val = int(''.join(['1']*size), 2)
				while count < cases and val <= max_val:
					number = "{0:b}".format(val)
					print(number)
					is_valid = True
					all_values = []
					for base in range(2, 11):
						value = int(number, base)
						all_values.append(value)
						if is_prime(value):
							is_valid = False
					if is_valid:
						count += 1
						divisors = []
						for nonprime in all_values:
							divisors.append(get_smallest_divisor(nonprime))
						o.write("{} {}\n".format(number, ' '.join(str(div) for div in divisors)))
					val += 2