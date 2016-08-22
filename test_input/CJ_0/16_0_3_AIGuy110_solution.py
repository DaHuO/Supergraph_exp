# coding: utf-8
import random

# lowest non-trivial factor
def lntFactor(n, maxSearch=None):
   high = n
   f=2
   while f<high:
     if maxSearch and f > maxSearch:
       return None
     if n%f==0:
       return f
     else:
       high = int(n/f) + 1
     f+=1
   return None

# Open Files
infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')


# The meat
jamBank = {}
cases = int( infile.readline() )
for case in range(1, cases+1):
   N, J = list( map(int, infile.readline().split(' ') ) )
   for j in range(J):
      print(str(j+1)+'/'+str(J), end='\r')
      while True:
        # make a random candidate
        digStr = '1'
        for i in range(N-2):
          digStr += random.choice(['0','1'])
        digStr += '1'

        # make sure we haven't already found this one
        if digStr in jamBank:
           continue
        
        # check if its a jam coin
        factors = []
        for base in range(2, 10+1):
          n = 0
          for place in range(N):
            n += base**place * int(digStr[N-place-1])
          f = lntFactor(n, 1000)
          if f == None:
            break
          else:
            factors.append(f)
        if len(factors) == 9:
          jamBank[digStr] = factors
          break

# Write output
keys = list(jamBank.keys())
outfile.write('Case #1:\n')  
for i in range( len(jamBank) ):
    key = keys[i]
    outfile.write(key+' '+' '.join(map(str, jamBank[key]))+'\n')

# Close up
infile.close()
outfile.close()
