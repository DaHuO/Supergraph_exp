import sys, math

# def digitSum(n):
#     s = 0
#     while(n>0):
#         r = n%10;
#         s += r
#         n /=10;
#     return s


# def isPrime(n):
#     if n == 0 or n == 1 or (n%2) == 0:
#         return 2
#     l = (math.ceil(math.sqrt(n)))
#     i = long(3)
#     if(digitSum(n) % 3 == 0):
#         return 3
#     while i<=l:
#         if ((n % i) == 0):
#             return i
#         i+=2
#     return 0


def isPrime(num, factorsList):
    if num == 2 or num == 3: return num
    if num < 2 or num%2 == 0:
        factorsList.append(2)
        return 2
    if num < 9: return num
    if num%3 == 0:
        factorsList.append(3)
        return 3
    r = 1000
    f = 5
    while f <= r:
        if num%f == 0:
            factorsList.append(f)
            return f
        if num%(f+2) == 0:
            factorsList.append(f+2)
            return (f+2)
        f +=6
    return 0


def main():
    t = int(raw_input())
    factorList = []
    for i in range(t):
        print "Case #" + str(i+1) + ": "
        n, j = map(int, raw_input().split())
        min = long(math.pow(2, n-1)) + 1
        max = long(math.pow(2, n))
        x = min
        while x<max:
            if j>0:
                lst = [0,0,0,0,0,0,0,0,0]
                if isPrime(x, factorList) != 0:
                    for l in range(0, n):
                        if (x & 1<<l) != 0:
                            for s in range(3, 10+1):
                                r = long(pow(s, l))
                                lst[s-2] += r
                res = 1
                lst[0] = x
                dec = lst[8]
                x+=2
                for l in range (0, 9):
                    lst[l] = isPrime (lst[l], factorList)
                    if(res != 0):
                        if lst[l]==0:
                            res = 0
                            
                if(res == 1):
                    j -= 1
                    print dec,
                    print " ",
                    for l in range(0, 9):
                        print lst[l],
                    print ""
            else:
                return
main()
