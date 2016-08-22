def turn_happy(stack):
  cur = None
  count = 0
  for i, pancake in enumerate(stack):
    if cur == None:
      cur = pancake
    else:
      if pancake != cur:
        stack = flip(stack[:i])+stack[i:]
        count += 1
        cur = pancake
  if(stack[0] == '-'):
    stack = flip(stack)
    count += 1
  return count


def flip(stack):
  flipped_stack = list()
  for pancake in stack:
    if(pancake == '+'):
      flipped_stack.append('-')
    else:
      flipped_stack.append('+')
  flipped_stack.reverse()
  return flipped_stack

results = list()
with open('B-large.in', 'r') as f:
  testcases = int(f.readline())
  for line in f:
    stack = [c for c in line]
    stack.remove('\n')
    results.append(turn_happy(stack))

with open('result.txt', 'w') as f:
  for i, res in enumerate(results):
    f.write('Case #'+str(i+1)+': '+str(res)+'\n')
