def convert(num, base):
    tmp=num
    ret=0
    pwr=1
    while tmp:
        ret += (pwr*(tmp%base))
        pwr*=10
        tmp/=base
    return ret

def checkPrime(num):
    i=2
    while i*i<=num and i<=10000:
        if num%i==0:
            return i
        i+=1
    return 0

def getNum(num, base):
    string = bin(num)[2:]
    return int(string, base)  

tc=input()
temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, tc+1):
    n, j = map(int, raw_input().split())
    print "Case #" + str(i) + ":"

    for k in range((1<<(n-1))+1, (1<<n), 2):
        flg=0
        for b in range(2, 11):
            div = checkPrime(getNum(k, b))
            if div==0:
                flg=1
                break
            else:
                temp[b-2] = div
        if flg!=0:
            continue;
        print bin(k)[2:],
        for l in range(0, 9):
            print temp[l],
        print
        j-=1
        if j==0:
            break
