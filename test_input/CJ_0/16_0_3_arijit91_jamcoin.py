import random

n = 32
cases = 500
t = 1

def random_string(n):
  digits = [ random.choice(['0', '1']) for i in xrange(n) ]
  digits[0] = '1'
  digits[-1] = '1'
  return "".join(digits)


print 'Case #1:'

while True:
  coin = random_string(n)
  factors = []
  ok = True
  for base in xrange(2, 11):
    num = int(coin, base)

    for k in xrange(2, 1000):
      if num % k == 0:
        factors.append(k)
        break

  if len(factors) == 9:
    print str(num) + " " + " ".join([str(x) for x in factors])

    t += 1
    #raw_input()

    if t == cases + 1:
      break
