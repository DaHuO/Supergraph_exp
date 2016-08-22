import math
import itertools

n = 6
j = 3
x = [0] * 11;

for i in range(2,11):
   x[i] = pow(i, n - 1) + 1;

for t in itertools.product([0, 1], repeat=n-2):
   y = list(x)
   for i in range(1, n-1):
      if not t[-i]:
         continue
      for k in range(2,11):
         y[k] += pow(k, i)
   sol = []
   for l in y[2::]:
      for p in range(2, int(math.sqrt(l))):
         if l % p == 0:
            sol += [p]
            break
      else:
         break
   if len(sol) == 9:
      print "1%s1" % "".join(map(str,t)), " ".join(map(str,sol))
      j -= 1
   if not j:
      break
