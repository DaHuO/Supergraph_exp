import itertools
import math

def as_base(n, b):
  ans = 0
  for x in n:
    ans *= b
    ans += x
  return ans

def divisor(n):
  for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
      return i
  return 0

def coinjam_divs(n):
  divs = []
  for x in (as_base(n, b) for b in xrange(2, 11)):
    div = divisor(x)
    if div == 0:
      return None
    else:
      divs.append(div)
  return divs
  
def test(n, j):
  coinjams = []  
  for p in itertools.product([0, 1], repeat=n-2):
    cj = (1,) + p + (1,)
    divs = coinjam_divs(cj)
    if divs is not None:
      coinjams.append((cj, divs))
      print len(coinjams)
    if len(coinjams) == j:
      return '\n'.join(fmt_jamcoin(jc) for jc in coinjams)

def fmt_jamcoin(jc):
  a = as_base(jc[0], 10)
  return '{} {}'.format(a, ' '.join(map(str, jc[1])))

def main():
  T = int(raw_input())
  NJ = []

  for t in xrange(T):
    NJ.append(map(int, raw_input().split()))

  for t, (n, j) in enumerate(NJ):
    print "Case #{}:\n{}".format(t+1, test(n, j))

if __name__ == '__main__':
  main()
