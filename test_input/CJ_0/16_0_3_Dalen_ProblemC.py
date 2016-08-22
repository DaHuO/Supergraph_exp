
import random
import math

INPUT_FILE = 'test.in';
OUTPUT_FILE = 'A-small-practice.out';
GENERATED = []

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

def generate_bin(length):
   bin = "1%s1" % ''.join(random.choice('01') for n in xrange(length))
   while bin in GENERATED:
      bin = "1%s1" % ''.join(random.choice('01') for n in xrange(length))
   return bin

def generate_divisors(bin):
   divisors = []
   for base in range(2,11):
      n = int(bin,base)
      for d in range(2,int(math.sqrt(n) + 1)):
         if n % d == 0:
            divisors.append(d)
            break
   return divisors

def algorithmA(N):
   prime = True
   bin = ""
   while prime:
      prime = False
      bin = generate_bin(N-2)
      for base in range(2,11):
         n = int(bin,base)
         if is_prime(n):
            prime = True
            break

   return bin + ' ' + ' '.join(map(str,generate_divisors(bin)))

def solve(data):
   tokens = map(int,data[0].split())
   result = '';
   for i in range(0,tokens[1]):
      result += '\n'+algorithmA(tokens[0])
   return result

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(1,len(lines)):
      result = solve([lines[i].strip(' \t\n\r')])
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()
#print generate_divisors("1001")