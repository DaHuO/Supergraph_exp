import math

def convert(n, b):
    cur = len(n) - 1
    num = 0
    for i in range(0,len(n)):
        if n[i] == '1':
            num += pow(b, cur)
        cur -= 1
    return num

def checkprime(nn):
    for i in prime:
        if (nn % i) == 0:
            if nn == i:
                return -1
            else:
                return i
    return -1
    
print "Case #1:"
n, j = 16, 50
n = int(n)
c = int(j)

f = open("50M_part1.txt", 'r')
prime = []
for line in f:
    for w in line.split():
        prime.append(int(w))

temp = pow(2,(n-2))
count = 0
for j in range(0, temp - 1):
    s = "{0:b}".format(j + temp) + "1"
    tobreak = False
    sol = [-1 for i in range(9)]        
    for k in range(2, 11):
        nn = convert(s, k)
        sol[k-2] = checkprime(nn)
        if sol[k-2] == -1:
            tobreak = True
            break
    if tobreak:
        pass
    else:
        print s,
        for pr in sol:
            print pr,
        print
        count += 1
        if count >= c:
            ##print "end", count, c
            break