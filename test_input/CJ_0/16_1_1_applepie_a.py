import sys
from collections import deque
lines = map(lambda x: x.strip(), sys.stdin.readlines())

N = int(lines[0])
for case in range(1, N+1):
  s = lines[case]
  best = deque()
  best.append(s[0])
  for c in s[1:]:
    if c >= best[0]:
      best.appendleft(c)
    else:
      best.append(c)
  print("Case #{0}: {1}".format(case, ''.join(best)))
     
