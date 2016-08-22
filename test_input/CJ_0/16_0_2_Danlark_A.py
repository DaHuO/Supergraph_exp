inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())

def findzero():
  for i in range(len(a) - 1, -1, -1):
    if a[i] == 0:
      return i
  return -1

def swap(k):
  p = []
  for i in range(k + 1):
    p.append(a[i])
  print(p)
  for i in range(k + 1):
    a[i] = (p[k - i] + 1) % 2

for test in range(1, t + 1):
  c = inf.readline().strip()
  a = []
  ans = 0
  for i in range(len(c)):
    if c[i] == '-':
      a.append(0)
    else:
      a.append(1)
  i = 0
  n = len(a)
  while i < n and a[i] == 0:
    i += 1
  if (i == n):
    print('Case #', test, ': ', 1, sep = '', file = ouf)
  else:
    if i != 0:
      ans += 1
    for j in range(i):
      a[j] = 1
    c = [1]
    k = 0
    for i in range(1, n):
      if a[i] == a[i - 1]:
        c[k] += 1
      else:
        c.append(1)
        k += 1
    ans += 2 * (len(c) // 2)
    print('Case #', test, ': ', ans, sep = '', file = ouf)

inf.close()
ouf.close()
