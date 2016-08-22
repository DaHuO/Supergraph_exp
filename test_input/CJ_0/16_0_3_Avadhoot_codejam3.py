import math
import itertools

class permiter:
    def __init__(self, n):
        self.n = n
        self.s=n*'0'

    def __iter__(self):
        return self

    def next(self):
        if self.s!='1'*self.n:
            i=int(self.s,2)
            i+=1
            temp=bin(i)[2:]
            self.s='0'*(self.n-len(temp))+temp
            return self.s
        else:
            raise StopIteration()
        
def cal_base(S):
    bases=list()
    bases.append(int(S,2))
    bases.append(int(S,3))
    bases.append(int(S,4))
    bases.append(int(S,5))
    bases.append(int(S,6))
    bases.append(int(S,7))
    bases.append(int(S,8))
    bases.append(int(S,9))
    bases.append(int(S,10))
    return bases
def div(x):
    if int(str(x)[-1])%2==0:
        return 2
    elif sum(map(int,list(str(x))))%3==0:
        return 3
    elif int(str(x)[-1])%5==0:
        return 5
    else:
        for i in range(2,int(math.sqrt(int(x)))):
            if (int(x) % i) == 0:
                return i
                break
            if i > 100000:
                break
        return 0
                
        
T=int(input())
for i in range(T):
    N,J=map(int,input().split(' '))
    print("Case #"+str(i+1)+":")
    S="1"+"0"*(N-2)+"1"
    #perms=itertools.permutations("0"*(N-2)+"1"*(N-2),(N-2))
    #print perms
    perms=permiter(N-2)
    notfound=True
    permlist=list()
    temp="0"*(N-2)
    while(J!=0):
        if temp not in permlist:
            permlist.append(temp)
            p="1"+"".join(temp)+"1"
            bases=cal_base(p)
            factors=list()
            for j in bases:
                d=div(j)
                if d==0:
                    notfound=True
                    break
                else:
                    factors.append(d)
                    notfound=False
            if not notfound:
                J-=1
                print(p,factors[0],factors[1],factors[2],factors[3],factors[4],factors[5],factors[6],factors[7],factors[8])
        temp=perms.next()
