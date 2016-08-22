from collections import deque
from itertools import product
inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')

t = int(inf.readline())

for test in range(1, t + 1):
  s = inf.readline().rstrip()
  last = len(s) - 1
  last1 = len(s) - 1
  ans = []
  st = set()
  for i in range(90, 64, -1):
    for j in range(last, -1, -1):
      if ord(s[j]) == i:
        ans.append(s[j])
        last1 = j
        st.add(j)
    last = last1
  for i in range(len(s)):
    if i not in st:
      ans.append(s[i])

  print('Case #', test, ': ', *ans, sep = '', file = ouf)

inf.close()
ouf.close()
