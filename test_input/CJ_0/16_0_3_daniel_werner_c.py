import math
import random
import itertools

def getDiv(n):

 if n <= 3:
  return False
  
 for i in range(2, 100):#int(math.floor(math.sqrt(n))) + 1):
  if n % i == 0:
   return i
   
 return False


def solve(n, j):

 seen = set()
 answers = []
 its = itertools.product("01", repeat=n-2)
 while len(answers) < j:
  test = "1" + "".join(its.next())
  test += "1"
  
  if test in seen:
   continue
  
  divs = [test]
  for base in range(2, 11):
   di = getDiv(int(test, base))
   if di:
    divs.append(str(di))
   else:
    break

  if len(divs) == 10:
   print len(answers)
   answers.append(divs)
  
  seen.add(test)
  
 return answers
  

name = "storage/emulated/0/codejam/C-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
 line = fi.readline().strip().split(" ")
 line = map(int, line)
 n = line[0]
 j = line[1]

 fout.write("Case #" + str(i + 1) + ": " + "\n")
 answers = solve(n, j)
 for a in answers:
  fout.write(" ".join(a) + "\n")
 print "Case #" + str(i + 1) + ": "
 for a in answers:
  print " ".join(a)

fi.close()
fout.close()