import math
import itertools
def main():
    f=open('input3.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        t=f.readline().rstrip('\n')
        [N,J]=t.split();
#        print N
#        print J
        lst=["".join(seq) for seq in itertools.product("01", repeat=int(N))]
#        print calculate(lst,int(J));
        testcases.append(calculate(lst,int(J)))
    fo=open('output3.txt','w+')
    for i in range(n):
#        print "Case #{0}".format(i+1)
        fo.write("Case #{0}:\n".format(i+1))
#        print testcases[i]
        for j in range(len(testcases[i][0])):
            lst=testcases[i][1][j]
#            print "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(testcases[i][0][j],lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8])
            fo.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(testcases[i][0][j],lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8]))

#    for i in range(n):
#        fo.write('Case #{0}: {1} \n'.format(i+1,testcases[i]))

def calculate(lst,J):
    nums=[]
    divisors=[]
    output=[nums,divisors]
    count=0
    for i in range(len(lst)):
        if lst[i][0]!='0' and lst[i][-1]!='0' and count<J:
#            print "num",lst[i]
            if baseCalculation(lst[i]):
                divisor=divisorCalculation(lst[i])
                if None in divisor:
                    continue
                else:
                    nums.append(lst[i])
                    divisors.append(divisor)
                    count=count+1
    return output        

def baseCalculation(num):
    for i in range(2,11):
        nbase=baseConvert(num,i)
        if checkPrime(nbase):
            return False
    return True

def baseConvert(num,base):    
    nbase=0
    for i in range(len(num)):
        nbase=nbase*base+int(num[i])
    return nbase
        
def checkPrime(n):
    for i in range(3, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def divisorCalculation(num):
    divisor=[]
    for i in range(2,11):
        nbase=baseConvert(num,i)
#        print nbase
        div=nontrivialDivisor(int(nbase),divisor)
        divisor.append(div)
    return divisor
    
def nontrivialDivisor(nbase,divisor):
    for i in range(3,int(math.sqrt(nbase))+1):
        if nbase%i==0 and i not in divisor:
            return i
            
if __name__=="__main__":
    main()