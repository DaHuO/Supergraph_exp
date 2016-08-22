# link: https://code.google.com/codejam/contest/dashboard?c=6254486#s=p2
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2016/round1A"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(str, line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
iLineNum=1
for iCase in xrange(int(inputData[0][0])):
  word=inputData[iLineNum][0]
  bestLastWord=""
  for ch in word:
    bestLastWord=ch+bestLastWord if ch+bestLastWord>bestLastWord+ch else bestLastWord+ch
  fileToWrite.write("Case #"+str(iCase+1)+": "+bestLastWord+"\n")
  iLineNum+=1
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
