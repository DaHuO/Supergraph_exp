def flipTilllastMinusIndex(S,lastMinusIndex):
  #print "Str:",S
  subStr = S[:lastMinusIndex+1]
  #print "subStr:",subStr
  flippedSubStr = ""
  for c in subStr:
    flippedSubStr += '+' if c == '-' else '-'
  #print 'flippedSubStr',flippedSubStr
  reS = flippedSubStr + S[lastMinusIndex+1:]
  #print "resStr:",reS
  return reS

def calculateMinFlips(S):
  fNo = 0
  while True:
    if S is not None:
      lastMinusIndex = S.rfind('-')
      if (lastMinusIndex == -1):
        break
      ##flip string till lastMinusIndex (including)
      S = flipTilllastMinusIndex(S,lastMinusIndex)
      fNo = fNo + 1
  return fNo


T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  S = raw_input()
  #print S,len(S),type(S)
  ans = calculateMinFlips(S)
  print"Case #{}: {}".format(i,ans)
