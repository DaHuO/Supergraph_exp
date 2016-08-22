def solve(cakes):
  slices = list(cakes)
  moves = 0
  done, l = 0, len(slices)
  while not done:
    cake = slices[0]
    i = 0
    if cake  == "+":
      while i < l and slices[i] == "+":
        slices[i] = "-"
        i += 1
      if i == l: 
        done = 1
      else:
        moves += 1
    elif cake == "-":
      while i < l and slices[i] == "-":
        slices[i] = "+"
        i += 1
      if i == l: 
        moves += 1
        done = 1
      else: 
        moves += 1
  return moves

T = input ()
for t in xrange (1, T + 1):
  cakes = raw_input ()
  print("Case #%i: %s" % (t, solve(cakes)))