t = int(raw_input())

for case in xrange(1, t+1):
  stack = list(raw_input())
  flips = 0
  while stack:
    flip_point = None
    start = stack[0]
    for x in range(1,len(stack)):
      if stack[x] != start:
        flip_point = x
        break
    else:
      if start == '-': flips+=1
      stack = []
    if flip_point:
      stack = stack[x:]
      flips += 1
  print "Case #{}: {}".format(case, flips)