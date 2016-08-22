#!/usr/bin/env python2.7

#input and output files
testfile=open("testlarge.txt", 'r')
outputfile=open("outputlarge.txt", 'w')

#number of trials that will be in file
numtests=testfile.readline()

#iterate through num of trials
for i in range(int(numtests)):
   T=testfile.readline()
   
   pancakes=[] #+=happy, -=sad

   #make array for pancakes
   for letter in T:
      pancakes.append(letter)

   #count number of switches and where the switches are
   first=pancakes[0]
   numchanges=0
   for p in range(1, len(pancakes)):
      second=pancakes[p]
      if first!=second:
         numchanges+=1
      first=second

   numchanges=numchanges-1

#starts with + and even num of changes
   if pancakes[0]=='+' and numchanges%2==0:
      flips=numchanges
   #starts with + and odd num of changes
   elif pancakes[0]=='+' and numchanges%2==1:
      flips=numchanges+1
   #starts with - and even num of changes
   elif pancakes[0]=='-' and numchanges%2==0:
      flips=numchanges+1
   #starts with - and odd num of changes
   elif pancakes[0]=='-' and numchanges%2==1:
      flips=numchanges
      
   outputfile.write("Case #{0}: {1}".format(i+1, flips))
   outputfile.write("\n")

#close files
outputfile.close()
testfile.close()      

