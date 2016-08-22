from math import sqrt;
import itertools
    
def perms(n):
    if not n:
        return
    count=0
    for i in range(2**n):
        count=count+1
        if(count>100000):
            break;
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, 1000000, 1))#int(sqrt(num)) + 1


t=int(input())
for i in range(t):
    print("Case #",i+1,":",sep="")
    fin_n, max_j= input().split()
    fin_n = int(fin_n)
    max_j= int(max_j)
    #print('fin',fin_n,type(fin_n),'max_j',max_j)
    #l=["".join(seq) for seq in itertools.product("01", repeat=fin_n-2)]
    l=list(perms(int(fin_n-2)))
    new_list=['1'+i+'1' for i in l]
    #print(new_list)
    for i in new_list:
        #print("the current entrant is",int(i))
        j=[]
        found=True
        #check(new_list)
        for m in range(2,11):
            if(found==False):
                break
            p=int(i,m)
            #print('p is', p, type(p))
            if(is_prime(int(p))):
                found=False
                break
            else:
                for z in range(2,int(p/2)):
                    if(p%z==0):
                        #print('z is',z)
                        j.append(z)
                        break
            #print('out of break')
        if(found==True):
            print(int(i),'',end="")
            for lma in j:
                print(int(lma),'',end="")
            print("")
            max_j= max_j-1
        if(max_j==0):
            break
         
