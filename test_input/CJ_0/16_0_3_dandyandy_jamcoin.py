import random

T = int(raw_input())
second_line = raw_input().strip().split(" ")
N = int(second_line[0])
J = int(second_line[-1])

def find_divisor(n):
  for i in range(2, 100000):
    if (n % i) == 0 and n != i:
      return i
  return 1

print "Case #1:"

already_used = set()

while J > 0:
  try_this = str(1) + str(''.join(random.choice("01") for i in range(N-2))) + str(1)
  if try_this in already_used:
    continue
  divisors = []
  for base in range(2, 11):
    curr = int(try_this, base)
    alph = find_divisor(curr)
    if (alph > 1):
      divisors.append(alph)
    else:
      break
  if len(divisors) < 9:
    continue
  else:
    print try_this, ' '.join(str(x) for x in divisors)
    J -= 1
    already_used.add(try_this)
