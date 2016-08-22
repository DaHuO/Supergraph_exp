import math
import sys

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def cache_primes(length):
  upper_bound = int('1' * length)
  for num in xrange(11, int(math.ceil(math.sqrt(upper_bound))), 2):
    for prime in PRIMES:
      if num % prime:
        break
      if prime <= math.sqrt(num):
        break
    else:
      PRIMES.append(num)


def stream_generator(start, stop, step=1):
  """Generates a stream of strs from start to stop in binary system."""
  for num in xrange(start, stop, step):
    yield str(bin(num))[2:]


def interpret_from_base(string, base):
  """Return value of the string decoding from the base system."""
  num = 0
  for digit in string:
    num = num * base + int(digit)
  return num


def get_a_divisor(value):
  """Gets a non-trivial divisor of value, None if no divisors are found."""
  num_str = str(value)
  sum_of_digits = sum(map(int, num_str))
  if sum_of_digits % 3 == 0:
    return 3
  if num_str[-1] in (0, 5):
    return 5
  if value % 2 == 0:
    return 2
  for divisor in PRIMES:
    if value % divisor == 0:
      return divisor


def find_jamcoins(length, count):
  strs = stream_generator(2 ** (length - 1) + 1, 2 ** length + 1, 2)
  jamcoins, generated = {}, 0

  for num_str in strs:
    if generated == count:
      break

    divisors = []
    for base in range(2, 11):  # [2, 11)
      value = interpret_from_base(num_str, base)
      divisor = get_a_divisor(value)
      if not divisor:
        break
      divisors.append(str(divisor))
    else:
      jamcoins[num_str] = divisors
      print num_str + ' ' + ' '.join(jamcoins[num_str])
      generated += 1
  print 'Generaged {0}'.format(generated)
  return jamcoins


def main():
  f_inp = open('C-large.in')
  f_out = open('C-large.out', 'w')
  inp = f_inp.read().split('\n')
  inp = inp[:-1]
  print inp
  cases = int(inp[0])
 # cases, length, count = map(int, sys.argv[1:4])
  for case in range(1,cases+1):
    length, count = map(int, inp[case].split())
    jamcoins = find_jamcoins(length, count)
    f_out.write("Case #"+str(case)+": \n")
    for j in jamcoins:
        f_out.write(str(j)+' ')
        for k in jamcoins[j]:
            f_out.write(str(k)+' ')
        f_out.write('\n')
    f_out.write('\n')

if __name__ == '__main__':
  main()
