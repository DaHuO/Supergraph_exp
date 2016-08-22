br = open('c.in')
pw = open('c.out', 'w')

def to_base_n(n, b):
  return sum([int(v) * (b ** i) for i, v in enumerate(n[::-1])])

def divisor(n):
  i = 2l

  while i ** 6 < n:
    if n % i == 0:
      return i

    i += 1

  return -1

n = 32
k = 500

pw.write('Case #1:\n')

for i in xrange(1l << (n - 1), (1l << n) - 1):
  if i % 2:
    s = bin(i)[2:]

    d = [-1 for j in range(11)]

    for j in range(2, 11):
      d[j] = divisor(to_base_n(s, j))

      if d[j] < 0:
        break

      if all([x > 0 for x in d[2:]]):
        pw.write(s + ' ' + ' '.join(str(x) for x in d[2:]) + '\n')
        print(s + ' ' + ' '.join(str(x) for x in d[2:]), k)
        k -= 1 

      if k <= 0: 
        exit()
        
pw.close
