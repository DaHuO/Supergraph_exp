from itertools import product
import sys
from math import ceil
inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = 1

def isprime(a):
  if a == 1:
    return 0
  for i in range(2, 10):
    if a % i == 0:
      return i
  return 0

print('Case #1:', file = ouf)

for test in range(1, t + 1):
  n, j1 = 32, 500
  ans1 = 0
  for posl1 in product([0, 1], repeat=n - 2):
    posl = [1]
    for i in range(len(posl1)):
      posl.append(posl1[i])
    posl.append(1)
    if (ans1 >= j1):
      break
    flag = True
    ans = []
    for j in range(2, 11):
      aj = 0
      for i in range(len(posl)):
        aj += j**i * posl[i]
      k = isprime(aj)
      if (k >= 2):
        ans.append(k)
      else:
        flag = False
    if flag:
      ans1 += 1
      for i in range(len(posl) - 1, -1, -1):
        print(posl[i], end ='', file =ouf)
      print(' ', end = '', file = ouf)
      print(*ans, file = ouf)

inf.close()
ouf.close()
