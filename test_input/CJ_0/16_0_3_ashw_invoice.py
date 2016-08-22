def jamcoin(T, N, M):
    noLength = N - 2
    maxNoPossible = '1'*noLength
    maxIntNo = int(maxNoPossible, 2) + 1
    count = 0
    l = dict()
    result = 'Case #'+str(T)+': \n'
    for i in xrange(0,maxIntNo):
        binaryVal = str(bin(i)).split("b")[1]
        if len(str(binaryVal)) <= noLength:
            binaryVal = '0'*(noLength - len(str(binaryVal))) + str(binaryVal)
            binaryVal = '1' + binaryVal + '1'  
        j = 2
        k = -1
        non_trivial = ''
        while j <= 10:
            baseNo = int(binaryVal, j)
            if baseNo in l:
                k = l[baseNo]
            else:
                k = check_prime(baseNo)
                l[baseNo] = k
            j = j+1
            if k != 1:
                non_trivial = non_trivial + str(k) + ' '
                continue
            else:
                break
        if k == 1:
            continue
        else:
            if count < (M-1):
                result = result + binaryVal + ' ' + non_trivial.strip() + '\n'
            else:
                result = result + binaryVal + ' ' + non_trivial.strip()
            count = count + 1
        if count == M:
            break
    print result
            
def check_prime(num):
    if num < 2:
        return 0
    if num == 2:
        return 1
    else:
        k = num
        div = 2
        while k > div:
            if num % div == 0:
                return div
            else:
                k = (num/div) + 1
            div = div + 1
        return 1
    
#jamcoin(1, 16, 50)            
t = int(input())
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    jamcoin(i, n, m)
