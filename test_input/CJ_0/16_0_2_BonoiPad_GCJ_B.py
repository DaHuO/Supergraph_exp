import copy

n = int(raw_input())

def solve(x,z):
  no = 0
  flag = 0
  memo = [x]
  while True:
   if flag == 1:
     break
   no = no + 1
   mlen = len(memo)
   for p in range(0,mlen):
    a = memo[p]
    for b in range(len(a)):
      buf = a[0:len(a)-b]
      buf = buf[::-1]
      buf = buf.replace("+","*")
      buf = buf.replace("-","+")
      buf = buf.replace("*","-")
      q = buf + a[len(a)-b:]

      if "-" in q:
        if q in memo:
          continue
        else:
          memo.append(q)
      else:
        print "Case #{}: {}".format(z+1,no)
        flag = 1
        return

for a in xrange(0, n):
  x = raw_input().strip()
  if "-" in x:
    solve(x,a)
  else:
    print "Case #{}: 0".format(a+1)

