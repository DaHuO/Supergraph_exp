import itertools
import gmpy2
import pyecm

def validate(jamcoin,divisors):
    outstrings = []
    for i,j in zip(range(2,11),divisors):
        jamcoin_ten = int(jamcoin,i)
        if gmpy2.is_prime(jamcoin_ten):
            return False
        outstrings.append(pyecm.factors(jamcoin_ten,False,True,10,1).__next__())
        # outstrings.append(factors.factors(jamcoin_ten).__next__()[0])
    print(jamcoin,end='')
    for i in outstrings:
        print(' ',end='')
        print(i,end='')
    print()
    return True

def jamcoin(case,length,num):
    print("Case #{0}:".format(case))
    count = 0
    for i in itertools.product('01',repeat=length-2):
        if count == num:
            break
        result = '1'+''.join(i)+'1'
        if validate(result,range(2,11)):
            count += 1
 
cases = int(input())
for i in range(1,cases+1):
    length,num = [int(i) for i in input().split()]
    jamcoin(i,length,num)
