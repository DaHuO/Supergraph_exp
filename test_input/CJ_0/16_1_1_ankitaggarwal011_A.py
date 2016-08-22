def solve(word):
  ans = word[0]
  for i in word[1:]:
    if i >= ans[0]:
      ans = i + ans
    else:
      ans += i
  return ans

T = input ()
for t in xrange (1, T + 1):
  word = raw_input ()
  print("Case #%i: %s" % (t, solve(word)))