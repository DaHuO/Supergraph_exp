import sys
from math import sqrt
import time

def make_jamcoins(filename):
  start = time.time()
  with open(filename) as f:
    T = int(f.readline().rstrip())
    for t in range(T):
      n, j = f.readline().rstrip().split(" ")
      n, j = int(n), int(j)
      output = {}
      num_jamcoins = 0
      start_num_str = '1'+'0'*(n-2)+'1'
      # print start_num_str
      while num_jamcoins < j:
        # num_jamcoins += j
        broken = False
        factors = []
        for base in range(2, 11):
          dec_num = make_decimal(start_num_str, base)
          num_is_prime, factor = prime_or_factor(dec_num)
          if num_is_prime:
            broken = True
            start_num_str = get_next_num_str(start_num_str)
            break
          else:
            factors.append(factor)
        if not broken:
          num_jamcoins += 1
          # print start_num_str
          output[start_num_str] = factors
          start_num_str = get_next_num_str(start_num_str)
          if not start_num_str:
            "All numbers of length N exhausted"
            return
      # print 'time taken:',time.time() - start
      print "Case #{}:".format(t+1)
      for key in output:
        string = key
        for s in output[key]:
          string += " "+str(s)
        print string

def get_next_num_str(num_str):
  if '0' not in num_str:
    return
  for i in range(len(num_str)-2, 0, -1):
    if num_str[i] == '0':
      return num_str[:i] + '1' + num_str[i+1:]
    elif num_str[i] == '1' and num_str[i-1] == '0':
      return num_str[:i-1] + '10' + num_str[i+1:]

def make_decimal(num_str, base):
  ans = 0
  for i in range(len(num_str)-1, -1, -1):
    if num_str[i] == '1':
      ans += base**(len(num_str) - 1 - i)
  return ans

def prime_or_factor(num):
  for i in range(2, int(sqrt(num))):
    if num % i == 0:
      return False, i
  return True, None

if __name__ == '__main__':
  make_jamcoins(sys.argv[1])
