def solve(letters):
  lastword = [letters[0]]
  for c in letters[1:]:
    if c < lastword[0]:
      lastword.append(c)
    else:
      lastword.insert(0, c)
    # print(lastword)
  return ''.join(lastword)

t = int(input())
for i in range(1, t + 1):
  w = input()
  print("Case #%d: %s" % (i, solve(w)))
