import math


def solve(line):
  length, amount = [int(i) for i in line.split()]
  coinjams = ['\n']

  for n in range(2**(length-1), 2**length):
    if n % 2 == 0: continue
  # for n in range(9, 10):
    n = '{0:b}'.format(n)
    divisors = [n]
    for b in range(2, 11):
      i = int(n, b)
      d = find_divisor(i)
      if d == 0:
        break
      divisors.append(str(d))
      # divisors.append(i) print representation

    if len(divisors) == 10:
      coinjams += divisors + ['\n']
      amount -= 1
    if amount == 0:
      break
  return '\n'.join(line.strip() for line in ' '.join(coinjams).split('\n'))

def find_divisor(n):
  if n % 2 == 0 and n > 2:
    return 2
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return i
  return 0

if __name__ == "__main__":
  n = int(input())

  for i in range(1, n+1):
    line = raw_input()
    print("Case #{0}: {1}".format(i, solve(line)))
