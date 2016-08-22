import collections as col

T = int(raw_input())

for x in range(1, T+1):
   S = raw_input()
   out = col.deque(maxlen=1000)
   out.append(S[0])
   for c in S[1:]:
       if c >= out[0]:
           out.appendleft(c)
       else:
           out.append(c)
   print "Case #%d: %s" % (x, ''.join(out))


       
