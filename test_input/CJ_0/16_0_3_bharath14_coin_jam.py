__author__ = 'bharath'
def isprime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return 0
    return 1

def factor(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return i
    return -1
def main():
    t=input()
    n,j=map(int,raw_input().split(" "))
    print n,j
    start=2**(n-1)
    if start%2==0:
        start+=1
    print "Case #1:"
    while j>0:
        while 1:
            num = int(bin(start)[2:])
            f=0
            if not isprime(start):
                for i in range(3,11):
                    if isprime(int(str(num),i)):
                        f=1
                        break
                if f==0:
                    print str(num),
                    for i in range(2,11):
                        print factor(int(str(num),i)),
                    break
            start+=2
        start+=2
        print ""
        j-=1
if __name__=="__main__":
    main()