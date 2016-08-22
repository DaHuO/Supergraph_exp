bases = range(2,11)

def convertToBase10(x, b):
    sum = 0
    for i, d in enumerate(x[::-1]):
        sum += int(d)*(b**i)
    return sum


        
def getDivisor(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return str(i)            
    return None

def isJamCoin(coin):
    if coin[0] != '1' or coin[-1] != '1':
        return False
    divisors = []
    for b in bases:
        x = convertToBase10(coin, b)
        div = getDivisor(x)
        if div == None:
            return False, None
        divisors.append(div)
    return True, divisors

def getNextJamCoin(coin):
    return bin(convertToBase10(coin, 2)+2)[2:]

t = int(input())

for c in range(t):
    print("Case #" + str(c+1) + ":")
    line = str.split(input())
    n = int(line[0])
    j = int(line[1])
    coin = "1" + (n-2)*"0" + "1"
    cnt = 0    
    while cnt < j:
        success, divisors = isJamCoin(coin)
        if success:
            print(coin + " " + " ".join(divisors))
            cnt += 1
        coin = getNextJamCoin(coin)