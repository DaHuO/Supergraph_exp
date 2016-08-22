import sys
 
def solve(str):
   minor = ''
   final = ""
   for c in str:
       if len(final) == 0:
          final = c
          continue
       if c < final[0]:
          final = final + c
       else:
          final = c + final
      
   return final
 
# main()
 
# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    # read 2 numbers
    msg = sys.stdin.readline().strip()
    # read several floats, keep the result in a list
 
    best = solve(msg)
    if len(best) != len(msg): print "PROBLEM!! in case", tc
    print 'Case #%d: %s' % (tc, best)
