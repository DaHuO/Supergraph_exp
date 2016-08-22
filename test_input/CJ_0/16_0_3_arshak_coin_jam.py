#!/usr/bin/python

import sys;

# Check if the given number if prime within the range or not.
def is_prime(n, r):
  k = 2;
  while (k <= r):
    if ((n % k) == 0): return k;
    k += 1;
  return -1;

small  = "C-small-attempt0.in"
large  = "C-large.in"
sample = "in.txt"

f = file(large);
n = int(f.next());    # Only one test case, so n is always 1.

for i in range(n):
  (k, j) = [int(x) for x in f.next().split()];
  a      = int(''.join(['0'] * (k - 2)), 2);
  b      = int(''.join(['1'] * (k - 2)), 2);
  ps     = [];
  m      = 0;
  fails  = [];    # All divisors are checked to be prime only within a small
                  # range i.e. 100. In case any divisor is failed to be proven
                  # that it is not prime, and if we do not have enough jamcoins
                  # found already, then the failed divisors will be checked
                  # again, but this time within the actual range
                  # i.e. divisor / 2.

  while (a <= b):
    # Create the string from current binary number.
    l = list(str(bin(a))[2:]);
    # Perform some padding to fix the length of the current number.
    pl = ''.join(['1'] + (['0'] * (k - len(l) - 2)) + list(str(bin(a))[2:]) + ['1']);

    # Check whether the generated numbers are prime or not.
    OK = True;    # This flag shows if the list of divisors has no prime.
    p  = [];      # List of all vallid divisors.

    # Check if there is any prime divisor with all bases.
    for x in [int(pl, x) for x in range(10 + 1)[2:]]:
      nn = is_prime(x, 100);
      if (nn == -1):
        # There is a prime divosor! Break the loop and set the flag to False.
        OK = False;
        break;
      p += [nn];
    if (OK):
      ps += [p + [pl]];
      m += 1;
    else: fails += [pl];

    # Check if we already have enough jamcoins.
    if (m >= j): break;

    a += 1;

  # There are not enough jamcoins, so one more round will be done on failed
  # divisors, but this time with the actual range for prime checking.
  if (m < j):
    for x in [int(pl, x) for x in range(10 + 1)[2:]]:
      nn = is_prime(x,  x / 2);
      if (nn == -1):
        # There is a prime divosor! Break the loop and set the flag to False.
        OK = False;
        break;
      p += [nn];
    if (OK):
      ps += [p + [pl]];
      m += 1;
    
  print "Case #%d:" % (i + 1);
  for x in ps:
    print x[-1] + ' ' + ' '.join(map(str, x[:-1]));

