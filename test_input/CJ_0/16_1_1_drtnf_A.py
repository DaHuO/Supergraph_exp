import sys

input = sys.stdin

def solve(s):
  out = s[0]
  for c in s[1:]:
    if c<out[0]:
      out = out+c
    else:
      out = c+out
  return out   

for case in range(int(input.readline())):
      S = input.readline().split()
      print("Case #"+ str(case+1) +":", solve(S[0]))
  
