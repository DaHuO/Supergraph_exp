alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def calculate(S):
  ans = S[0];
  largest = S[0]
  for i in S[1:]:
    if (alpha.index(largest)<=alpha.index(i)):
      ans = i + ans
      largest = i
    else:
      ans = ans + i
  return ans

T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  S = raw_input()  # read a list of integers, 2 in this case
  ans = calculate(S)
  print("Case #{}: {}".format(i, ans))
  # check out .format's specification for more formatting options
