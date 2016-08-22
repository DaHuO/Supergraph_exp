from math import ceil, sqrt
import random
def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def generate_prime_list(n):
    primes = set([2])
    i = 2
    while i < n:
      prime(i, primes)
      i += 1
    return primes

def is_prime(num, primes):
  print 'Prime check'
  s = num - 1
  t = 0

  if num < 2:
    return False

  if num in primes:
    return True

  for prime in primes:
    if not num % prime:
      return False

  while s % 2 == 0:
    s = s // 2
    t += 1

  for trials in range(5):
    a = random.randrange(2, num - 1)
    v = pow(a, s, num)
    if v != 1:
      i = 0
      while v != (num - 1):
        if i == t - 1:
          return False
        else:
          i += 1
          v = (v ** 2) % num
  return True

def get_next_num(current_num, N):
  bin_string = '{0:0' + str(N) + 'b}'
  return bin_string.format(int(current_num,2)+2)

def get_jamcoin(current_num, primes, N):
  is_jam = False
  print 'Getting jamcoins'
  while not is_jam:
    print 'Trying ', current_num
    is_jam = True
    divisors = [0]*9
    for n in range(2,11):
      int_val = int(current_num, n)
      if is_prime(int_val, primes):
        print 'Is prime, FAILED'
        current_num = get_next_num(current_num, N)
        is_jam = False        
        break
      else: 
        print 'Is not prime, finding divisors'
        for p in primes:
          if not int_val % p:
            divisors[n-2] = p
            break
        if divisors[n-2] == 0:
          is_jam = False
          print 'Is prime, FAILED'
          current_num = get_next_num(current_num, N)
          break
  print current_num, ' is a jamcoin'
  answer = current_num
  for d in divisors:
    answer += ' ' + str(d)
  return answer, current_num


def print_solution(ans, J):
  f = open('output_small.txt', 'w')
  f.write('Case #1:\n')
  for i in range(J):
    f.write(ans[i] + "\n")



if __name__ == '__main__':    
  N = 32
  num_primes = 7500

  primes = generate_prime_list(num_primes)
  print "Finished Prime List"
  J = 500
  answers = [0]*J
  current_num = "1" + "0"*(N-2) + "1"

  for i in range(J):
    answers[i], current_num = get_jamcoin(current_num, primes, N)
    current_num = get_next_num(current_num, N)
    print answers[i]
  print_solution(answers, J)  




    