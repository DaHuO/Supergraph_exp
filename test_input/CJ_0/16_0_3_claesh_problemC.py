#
# problemC.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

# Parser
def parser(fin):
    return fin.readInts()

    
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return 2
    if n < 9: return True
    if n % 3 == 0: return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return f
        if n % (f + 2) == 0: return f+2
        f += 6
    return True
    
# Solver
def solver(data):
    [N,J] = data
    
    answer = '\n'
    for i in xrange(2**(N-1),2**N-1):
        n = bin(i)[2:]
        if n[0] == '1' and n[-1] == '1':
            factors = []
            for base in [2,3,4,5,6,7,8,9,10]:
                result = isPrime(int(n,base))
                if result is True:
                    factors = []
                    break
                factors.append(result)
            if factors:
                J -= 1
                answer += n + ' ' + ' '.join(map(str,factors)) + '\n'
                print n, factors
            if J == 0:
                break
    return answer[:-1]
            

# Main
if __name__ == '__main__':
    with Timer('Problem C'):
        Problem(parser, solver).run()
