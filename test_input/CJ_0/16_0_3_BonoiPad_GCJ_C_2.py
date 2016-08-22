import gmpy2
from gmpy2 import mpz

def factors(n):
    result = set()
    n = mpz(n)
    i = 2
    while i < 1000000:
        div, mod = divmod(n, i)
        if not mod:
            return i
        i = gmpy2.next_prime(i)
    return False

x = int(raw_input())
n,j = map(int,raw_input().split(" "))
print "Case #1:"
no = 0

a = -1

while a < (1<<(n-2)):
  a = a + 1
  q = (a<<1) + 1 + (1<<(n-1))
  data = bin(q)[2:]
  flag = 0
  for base in range(2,10+1):
    if gmpy2.is_prime( int(data,base) ) == True:
      flag = 1
      break

  if flag == 1:
    continue

  ans = data
  for base in range(2,10+1):
    buf = factors(int(data,base))
    if buf == False:
      flag = 1
      ans = ""
      break
    ans = ans + " " + str(buf)

  if flag == 1:
    continue

  print ans
  no = no + 1
  if no == j:
    break


