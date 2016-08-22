
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  m = raw_input()
  l=list(m)
  ans=[]
  ans.append(l[0])

  for s in l[1:]:
      if s>=max(ans):
          ans.insert(0,s)
      else:
          ans.append(s)

  res="".join(ans)
  print "Case #{}: {}".format(i,res)
