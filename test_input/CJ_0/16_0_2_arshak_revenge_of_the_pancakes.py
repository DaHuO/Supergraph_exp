#!/usr/bin/python

import sys;

# Calculate minimum flips to make all pancakes happy recursively.
def min_flips(l):
  try:
    # Find the last occurence of non-happy pancake.
    i = (len(l) - 1) - l[::-1].index('-');
    # Perform a flip from the first element in stack until non-happy pancake.
    return 1 + min_flips(['-' if x == '+' else '+' for x in l[:i]]);
  except ValueError:
    # We are done! There is no non-happy pancake.
    return 0;

small  = "B-small-attempt0.in"
large  = "B-large.in"
sample = "in.txt"

f = file(large);
n = int(f.next());

for i in range(n):
  print "Case #%d: %d" % (i + 1, min_flips(list(f.next()[:-1])));

