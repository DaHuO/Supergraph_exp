import math
def evaluate(number, base,n):
    value = 0
    for y in range(n-1,-1,-1):
        value += (number>>y&1)*pow(base,y)
    return value

def get_devisor(number, prime_list):
    if number < 2000000:
        if prime_list[number] == True:
            return -1
    sqrt_num = int(math.sqrt(number))
    upper_bound = min(sqrt_num+1, 10000)
    for i in range(2, upper_bound):
        if number%i == 0:
            return i
    return -1

def setup_prime_list(prime_list):
    length = prime_list.__len__()
    for i in range(2, length):
        if prime_list[i] == None:
            prime_list[i] = True
        for j in range(2, length):
            now = i * j
            if now >= length:
                break
            prime_list[now] = False
    return prime_list

def get_next(jamcoin):
    return jamcoin+2

def printOut(jamcoin):
    print(bin(jamcoin))

if __name__ == "__main__":
    t = 1
    n = 0
    j = 0
    t = int(input(""))
    inputString = input("")
    n = int(inputString.split(" ")[0])
    j = int(inputString.split(" ")[1])
    prime_list = [False, None] * 1000000
    prime_list[2] = True
    prime_list = setup_prime_list(prime_list)
    jamcoin = 1
    jamcoin = jamcoin << (n-1)
    jamcoin += 1
    count = 0
    print("Case #1:")
    while (count<j):
        divisors = []
        fail = False
        for x in range(2,11):
            value = evaluate(jamcoin,x,n)
            divisor = get_devisor(value, prime_list)
            if divisor == -1 :
                fail = True
                break
            divisors.append(divisor)
        if not fail:
            count += 1
            print ("{0:b}".format(jamcoin), end="")
            for d in divisors:
                print (" "+str(d), end="")
            print ('') 
        jamcoin = get_next(jamcoin)