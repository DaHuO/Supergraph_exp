n = 0
l = []
def inp():
    n = int(input())
    for i in range(n):
        l.append([int(x) for x in input().split(" ")])

    for i in range(n):
        print("Case #",i+1,":",sep="")
        m(l[i][0],l[i][1])
    
    
def notPrime(x,b):    # x is binary str
    for i in range(2,int(int(x,b)**0.5)):
        #print("Checking with ",i)
        if(i%2 == 0):
            continue
        #if it's not prime in any base then return true
        #if(int(x,2)%i == 0 and int(x,3)%i == 0 and int(x,5)%i == 0 and int(x,6)%i == 0 and int(x,7)%i == 0 and int(x,10)%i == 0):
        #   return i
        
        if((int(x,b))%i == 0):
            return i
            
    return -1


def m(N,J):
    s = "1" + "0"*(N-2) + "1"  #replace later with k
    e = "1"*N
    j = 0
    
    for i in range(int(s,2),int(e,2)+1,2):

        b2 = notPrime(bin(i)[2:],2)
        b3 = notPrime(bin(i)[2:],3)
        b4 = notPrime(bin(i)[2:],4)
        b5 = notPrime(bin(i)[2:],5)
        b6 = notPrime(bin(i)[2:],6)
        b7 = notPrime(bin(i)[2:],7)
        b8 = notPrime(bin(i)[2:],8)
        b9 = notPrime(bin(i)[2:],9)
        b10 = notPrime(bin(i)[2:],10)

        if( b2 != -1 and b3 != -1 and b4!=-1 and b5 != -1 and b6 != -1  and b7 != -1 and b8!=-1 and b9!=-1 and b10 != -1):
            j+=1
            print(bin(i)[2:],end =" ") #,"    ", (i/(int(e,2)+1))*100,"%"
            print(b2,b3,b4,b5,b6,b7,b8,b9,b10,sep=" ")
            if(j==J):
                return
inp()
        
