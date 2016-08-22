T = int(raw_input().strip())
for C in range(1,T+1):
  print "Case #" + str(C) + ":",
  S = raw_input().strip()
  ans = ""
  for i in range(len(S)):
    if(i == 0):
      ans += S[i]
    elif(ord(S[i]) >= ord(ans[0])):
      ans = S[i] + ans
    else:
      ans += S[i]
  print ans
    
