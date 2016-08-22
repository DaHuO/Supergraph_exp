from sys import stdin

def express(coin, base):
    exp = 0
    multiplier = 1
    for i in coin:
        if i == '1':
            exp += multiplier
        multiplier *= base
    return exp

def find_divisor(number):
    for i in range(2, 100):
        if number % i == 0:
            return i
    return None

def check(coin):
    divisors = []
    for base in range(2, 11):
        divisor = find_divisor(express(coin, base))
        if not divisor:
            return None
        else:
            divisors.append(divisor)
    return divisors

def generate(n):
    coin = ['0'] * n
    coin[0] = '1'
    coin[-1] = '1'
    while True:
        i = 1
        while coin[i] != '0':
            coin[i] = '0'
            i += 1
        coin [i] = '1'
        yield coin

lines = stdin.readlines()
t = 0
for line in lines[1:]:
    t += 1
    print "Case #%d:" % t
    n, j = map(int, line.split(' '))
    generator = generate(n)
    while j > 0:
        coin = generator.next()
        divisors = check(coin)
        if divisors:
            print ''.join(reversed(coin)), ' '.join(map(str, divisors))
            j -= 1
