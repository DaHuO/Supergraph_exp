from sys import stdin, stderr
from random import randint

def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def divisor(n):
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return i
        if i > 9:
            return - 1
    return -1
    
    
def to_jamcoin(n):
    s = []
    while n != 0:
        s.append(str(n % 2))
        n //= 2
    return int(''.join(reversed(s)))
    
    
def random_jamcoin(length):
    jamcoin = [None] * length
    jamcoin[0] = 1
    jamcoin[length - 1] = 1
    for i in range(1, length - 1):
        jamcoin[i] = randint(0, 1)
    return int(''.join(map(str, jamcoin)))

def interpret(jamcoin, base):
    s = 0
    m = 1
    while jamcoin != 0:
        s += (jamcoin % 10) * m
        jamcoin //= 10
        m *= base
    return s
    

def solve_case():
    N, J = read_ints()
    
    result = []
    
    lo = 2 ** (N - 1) + 1
    hi = 2 ** N - 1
    jamcoins = set()
    while len(result) < J:
        ok = True
        #jamcoin = to_jamcoin(randint(lo, hi))
        jamcoin = random_jamcoin(N)
        if jamcoin in jamcoins:
            continue
        jamcoins.add(jamcoin)
        row = [0] * 10
        row[0] = jamcoin
        for i in range(2, 10):
            d = divisor(interpret(jamcoin, i))
            if d == -1:
                ok = False
                break
            row[i - 1] = d
        if ok:
            d = divisor(jamcoin)
            if d != -1:
                row[9] = d
                result.append(' '.join(map(str, row)))
                #print(len(result), result, file=stderr)
        #current += 2
            
    return result

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}:'.format(case))
        result = solve_case()
        for row in result:
            print(row)

        
if __name__ == '__main__':
    main()
    