import itertools as it
from math import sqrt; from itertools import count, islice

def main():
  fn = "input_cur.in"
  
  f = open(fn, 'r')
  data = f.readlines()
  f.close()
  nentry = int(data.pop(0))
  
  for d in data:
    print 'Case #'+str(data.index(d)+1)+':'
    n = int(d.split()[0])
    j = int(d.split()[1])
    combos = list(product([0,1],repeat=n))
    #print 'combos created'
    #print combos
    ncombos = []
    for item in combos:
      if item[0] != 0 and item[-1] != 0:
        ncombos.append(item)
    #print 'taking care of 0s in first and last index'
    cnt = 0
    mcombos = []
    for item in ncombos:
      #print ncombos.index(item)+1
      chkval = True
      for k in range(2, 11):
        testnum = str(int(''.join(str(x) for x in item), k))
        #if int(testnum[-1]) not in [0, 2, 4, 5, 6, 8]:
        if isPrime2(int(''.join(str(x) for x in item), k)):
            chkval = False
            break
      if chkval:
        mcombos.append(item)
        cnt+=1
        if cnt == j:
          break
    #print mcombos
    #print 'prime numbers removed'
    #print 'finding factors'
    #print combos
    #print '\n\n'
    factorlist = []
    cnt = 0
    for item in mcombos:
      #print 'Doing ---' +  str(mcombos.index(item) + 1)
      tmp = []
      tmp.append(''.join(str(x) for x in item))
      for k in range(2, 11):
        num = int(''.join(str(x) for x in item), k)
        factors = print_factors(num)
        tmp.append(factors[0])
      #print tmp
      factorlist.append(tmp)  
      cnt+=1
      if cnt == j:
        break
    #print len(factorlist)
    for item in factorlist:
      print ' '.join(str(x) for x in item)
  
def isPrime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
  
def isPrime2(x):
  tmp = []
  i = 2
  while i>0:
    if x % i == 0:
      return False  
    i+=1
    if i == 20:
      return True
  return True  

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step  
  
def print_factors(x):
  tmp = []
  i = 2
  while i>0:
    if x % i == 0:
      tmp.append(i)
      break
    i+=1
  return tmp

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
        result = result[len(result)/3:]
    #print len(result)
    #result = result[:len(result)/24]
    #print len(result)
    #print result
    #print 'getting prod'
    for prod in result:
      #print prod
      yield tuple(prod)
  
if __name__ == '__main__':
  main()  