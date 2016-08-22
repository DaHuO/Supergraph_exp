def base(ls, bs):
  vl = 0
  tot = bs**(len(ls) - 1)
  for i in ls:
    vl += int(i == '1') * tot
    tot /= bs
  return vl

j = int(raw_input())
for t in range(j):
  line = raw_input().split()
  nm = line[0]
  divs = line[1:]

  for i in range(2, 11):
    if base(nm, i) % int(divs[i - 2]) != 0 or base(nm, i) == int(divs[i - 2]):
      print "error %d: %s with %s in base %d" % (t + 1, nm, divs[i - 2], i)