import math

def all_bases(n):
   return [int(str(n), b) for b in range(2, 11)]

def is_prime(num):
   for i in range(2, int(math.sqrt(num)) + 2):
      if num % i == 0:
         return i
   return None

def next(n):
   # next int in format 1...1
   n = list(str(n))[::-1]

   c = n.count('1') - 2

   for i in range(1, len(n)-2):
      if n[i] != '1':
         c -= 1

         if c != 0:
            n[i] = '1'   
         else:
            print"?", i
            n = ['0' for x in n]
            print n
            n[0], n[-1], n[i] = '1', '1', '1'
            print n
         return int(''.join(n[::-1]))

   print "bah", n
   #return next(int(''.join(n[::1])) + 1)

def old_next(n):
   x = int(str(n), 2) + 1
   x = bin(x)[2:]
   
   return int(x) if x[-1] == '1' else old_next(int(x)) 

"""
n = int("1000001")
for i in range(26):
   print old_next(n), int(str(n), 2)
   #if next(n) != old_next(n):
   #   pass#print "warning!"

   n=old_next(n)
exit(0)
_init = "1" + 14*"0" + "1"
_end = "1" * 16


_init = "100001"
_end = "111111"
_end = int(_init) + 5
"""
L = 16 #6
K = 50 #3

_init = "1" + (L-2)*"0" + "1"
valid = []

n = int(_init, 2)
while True:
   
   d = [is_prime(x) for x in all_bases(bin(n)[2:])]
   if not any([x is None for x in d]):
      valid.append((n, d))

   n += 2
   if len(valid) == K:
      break

print "Case #1:"
for n, d in valid:
   print bin(n)[2:], ' '.join(map(str, d))

