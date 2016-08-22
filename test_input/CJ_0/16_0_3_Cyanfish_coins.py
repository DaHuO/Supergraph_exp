import jam
import math
import string
digs = string.digits

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
    x = int(x)
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return 0

def solve(case):
    N = case.readInt()
    J = case.readInt()
    j = 0
    k = int(math.pow(2, N - 1)) + 1
    result = "\n"
    while j < J:
        coinstr = int2base(k, 2)
        ok = True
        factors = []
        for base in range(2, 11):
            num = int(coinstr, base)
            f = factor(num)
            #print(coinstr, base, num, f)
            if f == 0:
                ok = False
                break
            factors.append(str(f))
        if ok:
            result += coinstr + " " + " ".join(factors) + "\n"
            j += 1
        k += 2
    return result

jam.run("C-small-attempt1.in", solve)
