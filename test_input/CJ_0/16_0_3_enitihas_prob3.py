import gmpy2 as gmp

def left_pad(string,num):
    length = len(string)
    if length==num:
        return string
    return "0"*(num-length) + string

def min_div(num):
    for i in range(2,num+1):
        if num%i==0:
            return i

def isJamCoin(string):
    reprs = [int(string,base) for base in range(2,11)]
    for rep in reprs:
        if gmp.is_prime(rep):
            return False
    answers = [None] * 9
    for i in range(9):
        answers[i] = min_div(reprs[i])
    return answers

test = int(input())
for it in range(test):
    n,j = [int(x) for x in input().split()]
    ct = 0
    nm = n-2
    n , nm = nm , n
    curNum = 0
    results = []
    while ct < j:
        toNum = '1' + left_pad(bin(curNum)[2:],n) + '1'
        res = isJamCoin(toNum)
        if res:
            results.append((toNum,res))
            ct+=1
        curNum+=1
    print("Case #{}:".format(it+1))
    for result in results:
        print(result[0],end=' ')
        for i in range(8):
            print(result[1][i],end=' ')
        print(result[1][8])
