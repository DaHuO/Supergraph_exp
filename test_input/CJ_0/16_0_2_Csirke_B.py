import sys

T = int(sys.stdin.readline())

for i in range(T):
  print "Case #{}:".format(i+1),
  pc = sys.stdin.readline().strip() + "+"
  flip = 0
  for j in range(len(pc)-1):
    if pc[j] != pc[j+1]:
      flip += 1
  print flip