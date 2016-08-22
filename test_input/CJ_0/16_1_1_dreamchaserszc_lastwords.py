import fileinput

class TestCase(object):
  def __init__(self, word):
    self.word = word

def findIndex(subword):
  #print "in findIndex " + subword
  subwordList = list(subword)
  index = len(subwordList) - 1
  highestAsciiIndex = index
  highestAsciiChar = subwordList[index]
  while index > -1:
    if ord(subwordList[index]) - ord(highestAsciiChar) > 0:
      print "Value for the difference " + str(ord(subwordList[index]) - ord(highestAsciiChar))
      highestAsciiChar = subwordList[index]
      highestAsciiIndex = index
    
    index = index - 1

  #print "found highest index is " + str(highestAsciiIndex) + " char is " + highestAsciiChar, subword
  return highestAsciiIndex

def recur(subword):

  if len(subword) == 0 or subword == '' or subword == "":
    return ""

  if len(subword) == 1:
    return subword

  indexOfHighestAscii = findIndex(subword)

  wordList = list(subword)
  print wordList[indexOfHighestAscii]
  print "calling recur with " + str(wordList[indexOfHighestAscii]) + " " + str(wordList[0:indexOfHighestAscii]) + " " +''.join(wordList[indexOfHighestAscii+1:]) 
  print str(wordList[indexOfHighestAscii]) + ''.join(wordList[indexOfHighestAscii+1:])

  #if indexOfHighestAscii == 1:
    #return str(wordList[indexOfHighestAscii]) + ''.join(wordList[indexOfHighestAscii+1:]) + str(wordList[0])

  return str(wordList[indexOfHighestAscii]) + recur(''.join(wordList[0:indexOfHighestAscii])) + ''.join(wordList[indexOfHighestAscii+1:]) 

def solve(t):

  return recur(t.word.strip())

start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue
    
  t = TestCase(line)
  testCases.append(t)

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


