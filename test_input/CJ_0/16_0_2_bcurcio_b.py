def solve(s):
  return reduce(lambda x,y: (y,x[1] + (1 if x[0]!=y else 0)) ,s+'+',(s[0],0))[1]

t = int(raw_input())
for x in xrange(1,t+1):
  s = raw_input()
  print 'Case #%d: %d'%(x,solve(s))
  
