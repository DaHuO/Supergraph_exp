num_cases = int(input())

for i in range(num_cases):
  word = input()
  ans = ""
  for c in word:
    if ans == "":
      ans = c
    elif c < ans[0]:
      ans = ans + c
    else:
      ans = c + ans
  print("Case #{}: {}".format(i+1, ans))
  