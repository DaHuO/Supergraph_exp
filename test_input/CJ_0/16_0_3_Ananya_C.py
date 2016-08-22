
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

N = 32
J = 500

def prime_factor(num):
  for p in primes:
    if num <= p:
      return 0
    elif num % p == 0:
      return p
  return 0

start = (1 << (N-1)) + 1
end = (1 << N)

while start < end and J > 0:
  prime_factors = []
  for base in range(2,11):
    num = int(bin(start)[2:],base)
    p = prime_factor(num)
    if p == 0:
      break
    else:
      prime_factors.append(str(p))
  if len(prime_factors) == 9:
    print bin(start)[2:], " ".join(prime_factors)
    J -= 1
  start += 2
