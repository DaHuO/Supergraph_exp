import sys
lines = map(lambda x: x.strip(), sys.stdin.readlines())
N = int(lines[0])
for case in range(1, N+1):
  pancakes = lines[case]
  plus_flips = 0 if pancakes[0] == '+' else 1
  minus_flips = 1 if pancakes[0] == '+' else 0
  for pancake in pancakes[1:]:
    if pancake == '+':
      minus_flips = plus_flips + 1
    else:
      plus_flips = minus_flips + 1
  print("Case #{0}: {1}".format(case, plus_flips))
  
