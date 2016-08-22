from math import sqrt

def divisor(x):
  if(x == 2):
    return -1
  for d in range(2,int(sqrt(x))+1):
    if(x%d == 0):
      return d
  return -1

def is_jam(test):
  ans = []
  for base in range(2,11):
    x = int(test,base)
    div = divisor(x)
    if(div == -1):
      return []
    ans.append(div)
  return ans
    

T = int(raw_input().strip())
for t in range(1,T+1):
  print "Case #" + str(t) + ":"
  N,J = raw_input().strip().split()
  N = int(N)
  J = int(J)
  for i in range(2**(N-2)):
    if(J == 0):
      break;
    tmp = bin(i)[2::]
    while(not(len(tmp) == N-2)):
      tmp = '0' + tmp
    test = '1' + tmp + '1'
    ans = is_jam(test)
    if(len(ans) == 9):
      print test,
      for div in ans:
        print div,
      print ""
      J -= 1
