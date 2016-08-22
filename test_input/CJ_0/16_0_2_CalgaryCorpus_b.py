import sys
 
# len - len(x)
# dict = {}
#  for k in dict.keys()
#  del dict[k]
#  k in dict -> True, False   # <=> k in dict.keys()
 
 
# myset = set(mylist)
#  element in myset -> True | False
# mycharset = set(mystring)
#  set1 - set2  set1 has it and set2 does not
#  set1 | set2  union
#  set1 & set2  intersection
#  set1 ^ set2  xor  (set1 has it or set2 has it, not both)
 
def flipchar(c):
   if c == '-': return '+'
   return '-'

def flip(s):
   if len(s) == 0: return s
   s2 = ''.join([ flipchar(c) for c in list(s) ])
   return s2[::-1]

def h(s):
   l = len(s)
   if l == 0 or s.find('-') == -1: 
      return 0

   if s[-1] == '+':
   
      revs = s[::-1]
      revrevs = revs[revs.find('-'):][::-1]
      s = revrevs

   # los - iniciales se flipean con los ultimos, cuentan como 1 flip
   if s[0] == '-': 
      return 1 + h(flip(s))

   # hay un + al inicio, removamos todos los + al inicio y sumemos 1
   posm = s.find('-')
   return 1 + h(s[posm:])


def solve(p):
    return h(p)
 
 
# main()
 
# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    p = sys.stdin.readline().strip()

    best = solve(p)
    print 'Case #%d: %d' % (tc, best)
