#!/usr/bin/env python2.7

#int(binary string, base) will give int val of binary
#'{0:08b}'.format(int) will change int to 8bit binary

#isprime function from: https://www.daniweb.com/programming/software-development/code/462120/isprime-function-python
def isprime(val):

   #2 is prime
   if val==2:
      return True

   #if val is 1, 0 or neg or even (val&1 returns 0 if even, 1 if odd)
   elif val<2 or not val & 1:
       return False

   #check odd numbers up to sqrt(val)
   for i in range(3, int(val**0.5)+1, 2):
      if val%i==0:
         return False

   return True

def finddivisor(val):
   i=2
   while i>0:
      if val%i==0:
         return i
      else:
         i+=1


#input and output files
testfile=open("testsmall.txt", 'r')
outputfile=open("outputsmall.txt", 'w')

#num of trials
numtests=testfile.readline()

#list of bases
bases=[2, 3, 4, 5, 6, 7, 8, 9, 10]
#make dictionary of divisors for each base({jamcoinval:{base:div, base:div}})
divisors={}

#iterate through num of trials
for i in range(int(numtests)):
   T=testfile.readline().split(' ')
   N=int(T[0])
   J=int(T[1])

   #iterate through possible jamcoin values of length N
   #bin function returns string as '0b...' so need [2:]
   i=1
   while i>0:
      #make jamcoin value
      binaryval='%0*d' % (N, int(bin(i)[2:]))
      binarylist=list(binaryval)
      binarylist[0]='1'
      jamcoin="".join(binarylist)
      divisors[jamcoin]={}

      #go through all bases to check for true jamcoin
      for base in bases:
         value=int(jamcoin, base)
	 #if value is prime, not a jamcoin, continue to next jamcoin
	 if isprime(value):
	    del divisors[jamcoin]
	    break
	 #if value is not prime, get a divisor and add {base, divisor} to dictionary and append value to truejamcoins
	 else:
	    divisor=finddivisor(value)
	    divisors[jamcoin][base]=divisor
	 #end while loop if enough jamcoins found
      if len(divisors)>=J:
	 i=-10

      #increment i
      i+=2

#make outputfile
outputfile.write("Case #1:")
outputfile.write("\n")
for coin in divisors:
   outputfile.write(coin+" ")
   sortedbases=sorted(divisors[coin].keys())
   for b in sortedbases:
      outputfile.write(str(divisors[coin][b])+' ')
   outputfile.write("\n")


#close files
outputfile.close()
testfile.close()
