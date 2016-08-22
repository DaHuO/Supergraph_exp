other_start = list('1000000000000001')
start = list('100001')

def increment(s):
  for i in range(len(s)-2,0,-1):
    if s[i] == '0':
      s[i]='1'
      break
    else:
      s[i]='0'

def base_n(n):
  s = other_start
  res = 0
  j = 0
  for i in range(len(s)-1,-1,-1):
    if s[i] == '1':
      res = res + n**j
    j = j + 1
  return res

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def find_factor(n):
  for i in range(2, int(n**.5)+1):
    if n % i == 0:
      return i

def solve(n,j):
  jamcoins = []
  bases = [n+2 for n in range(9)]
  while len(jamcoins) < j:
    base_ns = map(base_n,bases)
    is_primes = map(is_prime, base_ns)
    if True not in is_primes:
      jamcoins.append(base_ns)
    increment(other_start)
  return jamcoins

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\inputs.txt') as r:
    case = 1
    jcoins = solve(other_start,50)
    solved = ''
    for jc in jcoins:
      mults = ' '.join(map(str,map(find_factor,jc)))
      solved = solved + str(jc[-1]) + ' ' + mults + '\n'
    w.write('Case #1:\n' + solved)

