#!/usr/bin/env python

import random
import itertools

def before(s, c):
  return c + s

def after(s, c):
  return s + c

def random_choice(s):
  mapping = {0: after, 1: before}
  ns = s[0]
  for c in s[1:]:
    i = random.choice([0,1])
    ns = mapping[i](ns, c)
  return ns

def all_permutations(s, p):
  mapping = {0: after, 1: before}
  ns = s[0]
  for i, c in zip(p, s[1:]):
    ns = mapping[int(i)](ns, c)
  return ns

def foo(s):
  # c = '10' * ((len(s)//2 + len(s)//2%2) + 1)
  # l = []
  # for p in itertools.permutations(c):
  #   l.append(all_permutations(s, p))
  l = [random_choice(s) for _  in xrange(100000)]
  return sorted(l)[-1]


if __name__ == '__main__':
  t = int(raw_input())  # read a line with a single integer

  for case in xrange(1, t + 1):
    s = str(raw_input())

    print "Case #{0}: {1}".format(case, foo(s))
