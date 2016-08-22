# 2016 Africa Qualification Round - C. Coin Jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2

from math import sqrt

def pad_num(s, width):
    diff = width - len(s)
    if diff <= 0:
        return s
    else:
        return '0'*diff + s

def make_coins(n):
    i = 0
    while i < 2**(n-2):
        inner = '{0:b}'.format(i)
        yield '1%s1' % (pad_num(inner, n-2))
        i += 1

def find_divisors(n):
    result = {}
    for base in range(2, 11):
        num = int(n, base)
        magic_num = 11
        
        for i in range(2, magic_num+1):
            if num % i == 0:
                if not result.get(n):
                    result[n] = []
                if i in result[n]:
                    continue
                else:
                    result[n].append(i)
                    #print n, 'in {:2d}'.format(base), '= {:16d}'.format(num), '% {:2d}'.format(i), '= {:1d}'.format(num%i)
                    break
    #print result
    return result

def is_real_coin(coin):
    divisor_dict = find_divisors(coin)
    for key in divisor_dict:
        if len(divisor_dict[key]) == 9:
            real_coin = [key]
            content = map(str, divisor_dict[key])
            real_coin.extend(content)
            return ' '.join(real_coin)
        

def solve(n, j):
    real_coins = []
    for coin in make_coins(n):
        coin = is_real_coin(coin)
        if coin:
            real_coins.append(coin)
            if len(real_coins) >= j:
                return real_coins

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    (n, j) = [int(n) for n in input.readline().split()]
    results = solve(n, j)

    result_output = 'Case #%s:\n' %(case)
    
    for r in results:
        result_output += r + '\n'

    print result_output
    print len(results)
    output.write(result_output)

input.close()
output.close()
