# Library available from pypi https://pypi.python.org/pypi/pyprimes/
from pyprimes import isprime

N = None
J = None

with open('C-large.in', 'r') as f:
  testcases = int(f.readline())
  values = f.readline().split(' ')
  N = int(values[0])
  J = int(values[1])

print 'VALUES LOADED - N:' + str(N) + ' J:' + str(J)

results = list()
coins = list()
counter = 0
pos = ''
done = False

while len(pos[2:]) <= N:
  pos = bin(counter)
  counter += 1

  if len(pos[2:]) <= N-2:
    padding = '0'*((N-2) - len(pos[2:]))
    coin = '1'+padding+pos[2:]+'1'
    for i in range(2, 11):
      num = int(coin, i);
      if isprime(num):
        print coin + ' IS NOT A JAMCOIN'
        break
      if i == 10:
        divisors = [coin]
        for i in range(2, 11):
          skip = True
          for j in range(2, 10000):
            if int(coin, i) % j == 0:
              divisors.append(j)
              skip = False
              break
          if skip:
            print 'SKIPPING COIN ' + coin
            break
        if len(divisors) == 10:
          print 'ADDING THE ' + str(len(results)) + ' COIN ' + coin
          results.append(divisors)
        if len(results) == J:
          done = True
          break
    if done == True:
      break

print results

with open('result-c-big.txt', 'w') as f:
  f.write('Case #1:\n')
  for jamcoin in results:
    for item in jamcoin:
      f.write(str(item) + ' ')
    f.write('\n')
