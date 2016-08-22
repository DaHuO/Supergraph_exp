T = int(raw_input())
for curcase in range(1,T+1):
  S = raw_input() + '+'
  count = 0
  for i in range(0, len(S)-1):
    if S[i] != S[i+1]:
      count += 1
  print "Case #" + str(curcase) + ":", count
