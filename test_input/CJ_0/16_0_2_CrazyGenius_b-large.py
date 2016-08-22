T = int(raw_input().strip())
for t in range(1,T+1):
  print "Case #" + str(t) + ":",
  inp = raw_input().strip()
  stack = [inp[0]]
  for s in range(1,len(inp)):
    if(inp[s] != inp[s-1]):
      stack.append(inp[s])
  if(len(stack) == 1):
    if(stack[0] == '+'):
      ans = 0
    else:
      ans = 1
  else:
    ans = len(stack) - 2
    if(stack[len(stack)-1] == '-'):
      ans += 2
    else:
      ans += 1
  print ans
