import sys, math


def generateJamcoins(N, howMany):
    
    coins = {}
    coin = (1 << (N - 1)) | 1
    maxCoin = (1 << N) - 1
    
    while (coin < maxCoin) and (len(coins) < howMany):
        
        if len(coins) % 50 == 0:
            print('Generated {} coins.'.format(len(coins)))
        
        divisors = []
        for base in range(2, 11):
            divisor = findDivisor(asBase(coin, base))
            if divisor:
                divisors.append(divisor)
            else:
                break
        if len(divisors) == 9:
            coins[coin] = divisors
        
        coin += 2
    
    return coins


def findDivisor(n):
    
    if n % 2 == 0:
        return 2
    
    s = int(math.sqrt(n))
    for x in range(3, s + 1, 2):
        if n % x == 0:
            return x
    
    return None


def asBase(dual, base):
    
    if base == 2:
        return dual
    
    x = 0
    b = 1
    while dual != 0:
        x += (dual & 1) * b
        b *= base
        dual = dual >> 1
    return x


if (__name__ == '__main__') and (len(sys.argv) == 4):
    N = int(sys.argv[1])
    howMany = int(sys.argv[2])
    coins = generateJamcoins(N, howMany)
    with open(sys.argv[3], 'w') as fout:
        fout.write('Case #1:\n')
        for coin, divisors in coins.items():
            fout.write('{:b} {}\n'.format(coin, ' '.join(str(d) for d in divisors)))