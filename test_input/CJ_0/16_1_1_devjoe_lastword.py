import sys
sys.setrecursionlimit(1001)

def find_firsts(s):
  #find the sequence of positions within s that should be placed at the front.
  maxs=max(s)
  pos=s.rfind(maxs)
  if pos==0:
    return [0]
  return find_firsts(s[:pos])+[pos]

t=input()
for j in xrange(t):
  s=raw_input().strip()
  firsts=find_firsts(s)
  #build result
  res=""
  fi=0
  for k in xrange(len(s)):
    if fi<len(firsts) and k==firsts[fi]:
      fi+=1
      res=s[k]+res
    else:
      res=res+s[k]
  print "Case #"+str(j+1)+": "+res
  

  
