N = 32
J = 500
primes = [2]
G = 100000
np = [False]*G

for i in xrange(4,G,2):
  np[i] = True

for i in xrange(3,G,2):
  if not np[i]:
    for j in xrange(i*i,G,i):
      np[j] = True
    primes.append(i)

d = 0
for i in xrange(1<<(N-2)):
  if (bin(i).count("1")+2)%3:
    continue
  v = [True]
  dv = []
  for j in xrange(N-2):
    v.append((((1<<j)&i) > 0))
  v.append(True)
  #print i, v[::-1]
  g = True
  for j in xrange(2,10):
    b = 1
    bg = True
    e = j
    for k in xrange(1,N):
      if v[k]:
        b += e
      e *= j
    #print " ", b
    for k in primes:
      if k >= b:
        break
      if b % k == 0:
        bg = False
        dv.append(k)
        break
    if bg:
      g = False
      break
  if g:
    s = ""
    for j in xrange(N-1,-1,-1):
      s += "1" if v[j] else "0"
    for j in dv:
      s += " " + str(j)
    print s, "3"
    d += 1
    if d == J:
      break
print d
