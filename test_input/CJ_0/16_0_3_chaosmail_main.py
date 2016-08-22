import fs
import math
import signal
from functools import lru_cache

def signal_handler(signum, frame):
    raise Exception("Timed out!")

@lru_cache(maxsize=None)
def is_prime(n):
  if n % 2 is 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)) 

@lru_cache(maxsize=None)
def divisor(n):
  if n % 2 is 0:
    return 2
  return next((i for i in range(3, int(math.sqrt(n)) + 1, 2) if n % i is 0))

def is_jamcoin(raw_num):
  for basis in range(2, 10 + 1, 1):
    if is_prime(int(raw_num, basis)):
      return False
  return True

def get_divisors(raw_num):
  return [divisor(int(raw_num, basis)) for basis in range(2, 10 + 1, 1)]

def get_jamcoin(length):
  for i in range(0, 2**(length-2)):
    yield '1{num:0{width}b}1'.format(num=i, width=length-2)

def solve(input):
  signal.signal(signal.SIGALRM, signal_handler)
  cols = input.split(' ')
  N = int(cols[0])
  J = int(cols[1])
  output = ""
  coins = set()
  for coin in get_jamcoin(length=N):
    signal.alarm(1)
    try:
      if is_jamcoin(coin) and coin not in coins:
        coins.add(coin)
        output += "%s %s\n" % (coin, " ".join(map(str, get_divisors(coin))))
        print("Found coin %i" % len(coins))
    except Exception as e:
      print(e)
    if len(coins) >= J:
      break
  else:
    print("Error occurred, not enough coins found!")
    exit(-1)

  return output

if __name__ == '__main__':
  IN_NAME = 'input.txt'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  for i, row in enumerate(rows):
    # Skip first row (contains number of entries)
    if i == 0: continue
    # Skip last row (contains only \n)
    if i == len(rows) - 1: continue
    solution += 'Case #%i:\n%s' % (i, str(solve(row)))

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)