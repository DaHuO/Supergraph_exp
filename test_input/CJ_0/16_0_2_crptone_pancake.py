from itertools import groupby 

f = open('pancake-large.txt')
g = open('pancake.out', 'w')
lines = f.readlines()
for i in range(1,len(lines)):
  pancakes = lines[i].strip()
  gr = ''.join(c for c, _ in groupby(pancakes))
  if gr[-1] == '-':
    ans = len(gr)
  else:
    ans = len(gr) - 1
  g.write('Case #' + str(i) + ': ' + str(ans) + '\n')
  

f.close()
g.close()
