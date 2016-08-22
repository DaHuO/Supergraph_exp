T = int(raw_input())
for i in range(1, T+1):
  seq = raw_input()
  ans = ""
  for c in seq:
    if ans == "":
      ans = ans + c
      continue
    if c < ans[0]:
      ans = ans + c
    else:
      ans = c + ans
  print "Case #{0}: {1}".format(i, ans)
