def flip(num, pancakes):
  t = ['-' if n == '+' else '+' for n in reversed(pancakes[:num])]
  return ''.join(t) + pancakes[num:]
def flips(pancakes):
  if pancakes.count('-') == 0: return 0
  h = -1
  for c in pancakes:
    if c == '+':
      h += 1
    else:
      break
  return 1 + flips(flip((h + 1) if h != -1 else (1 + pancakes.rfind('-')),pancakes))
tests = int(input(''))
for n in range(tests):
  print ('Case #' + str(n+1) + ": " + str(flips(raw_input(''))))