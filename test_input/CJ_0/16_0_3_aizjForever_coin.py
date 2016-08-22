def to_bin(i,N):
    res = bin(i)
    res = res[2:]
    while (len(res) < N - 2):
        res = "0" + res
    res = "1" + res + "1"
    return int(res)
def to_base_10(num,i):
    count = 0;
    res = 0
    while (num > 0):
        res += (num % 10) * (i ** count)
        num //= 10
        count += 1
    return res
def is_prime(n):
    if (n % 2 == 0):
        return (False,2)
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return (False,factor)
    return (True,None)
def is_prime_base(num,i):
    a = to_base_10(num,i)
    (b,L) = is_prime(a)
    if b:
        return (True,None)
    return (False,L)


def is_coin(num):
    res = []
    for i in range(2,11):
        (b,L) = is_prime_base(num,i)
        if b:
            return (False,None)
        res.append(L)
    return (True,res)

def solve_coin(N,J):
    res = ""
    count = 0
    for i in range(2**(N-2)):
        num = to_bin(i,N)
        (b,L) = is_coin(num)
        if b:
            res += "%d " % num
            for c in L:
                res += "%d " % c
            res = res[:-1]
            res += "\n"
            count += 1
            if count == J:
                return res[:-1]

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsRead = readFile("C-small-attempt0.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    N = int(c.split(" ")[0])
    J = int(c.split(" ")[1])
    res = solve_coin(N,J)
    contentsToWrite += "Case #%d: " % count
    contentsToWrite += "\n"
    contentsToWrite += res + "\n"
    count += 1
writeFile("out.txt",contentsToWrite)


