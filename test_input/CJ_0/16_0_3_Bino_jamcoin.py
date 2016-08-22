import random as rd

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return 1

def base_rep(s, base):
    n = len(s)
    num = 0
    sig = 1
    for i in range(n):
        if s[n-i-1] == '1':
           num = num + sig
        sig = sig*base
    return num

def isJamcoin(s):
    print("s: " + s)
    divisors = []
    for i in range(2,11):
        number = base_rep(s, i)
        #print("Number: " + str(number))
        div = isprime(number)
        if div == 1:
            return []
        divisors.append(div)
    return divisors

def toBinary(N,length):
    s = "{0:0"+str(length)+"b}"
    #print(s)
    return s.format(N)

def jamcoin(N,J):
    jamcoins = []
    while(len(jamcoins) < J):
        s = '1'+toBinary(rd.getrandbits(N-2),N-2)+'1'
        divs = isJamcoin(s)
        if len(divs) > 0:
            string = str(divs).replace(",","").replace("[","").replace("]","")
            string = s+" "+string
            if not (string in jamcoins):
                jamcoins.append(string)
    return jamcoins

if __name__ == "__main__":
    input = "C-small-attempt0"
    f = open(input + ".in")
    output = open(input + ".out", "w")
    cases = int(f.readline())
    for i in range(cases):
        line = f.readline().split()
        N = int(line[0])
        J = int(line[1])
        coins = jamcoin(N,J)
        output.write("Case #" + str(i+1)+ ":\n")
        for coin in coins:
            output.write(coin + "\n")
    f.close()
    output.close()