#!/usr/bin/env python3

import sys
import re

def maneuver(pancakes):
  matches = re.findall(r'((\+|-)\2*)', pancakes)
  groups  = [m[0] for m in matches]
  total   = len(groups)
  last    = groups[-1]

  if (last.endswith("-")):
    return total
  else:
    return total - 1


file  = open(sys.argv[1])
total = int(file.readline())

for i in range(1, total + 1):
  pancakes = file.readline().rstrip()
  result   = maneuver(pancakes)
  print("Case #%d: %s" % (i, result))
