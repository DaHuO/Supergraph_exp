import copy
import sys
import math


def parse_case(instrm):
    return [int(i) for i in instrm.readline().strip().split()]


def crivello_di_erastotene(bigN):
    divisors = [None]*bigN
    for i in range(2, int(math.sqrt(bigN)) + 1):
        if divisors[i] is not None:
            continue
        
        for j in range(2, bigN):
            tmp = j*i
            if tmp >= len(divisors):
                break
            if divisors[tmp] is None:
                divisors[tmp] = i
    return divisors

def tobinary(num):
    s = ""
    while num > 0:
        s += str(num & 1)
        num = num >> 1
    return s[::-1]   

def shift_carry(dlist, base=10):
    carry = 0
    for i in range(len(dlist)):
        dlist[i] += carry
        carry = dlist[i] // base
        dlist[i] = dlist[i] % base
    assert carry == 0, "not enough digits"

def change_base(base, num):
    # find out how many digits the number will contain at most
    s = tobinary(num)
    if base == 10:
        return s
    nbits = len(s)
    ndigits = int(math.ceil((nbits + 1)*math.log10(base)))
    assert ndigits >= 1 and base > 1 and base < 10

    sol = [0]*ndigits
    exp = [0]*ndigits
    exp[0] = 1

    for b in s[::-1]:
        if b == "1":
            for i in range(ndigits):
                sol[i] += exp[i]
        for i in range(ndigits):
            exp[i] *= base    
        shift_carry(sol)
        shift_carry(exp)
    
    while sol[-1] == 0:
        sol.pop()

    return "".join(str(d) for d in sol[::-1])
    
def solve_case(case):
    N, J = case
    assert N > 2
    # compute all prime numbers from 1 to 2^N-1
    bigN = 1 << N
    divisors = crivello_di_erastotene(bigN)
    smallN = 1 << (N-2)
    mask = (1 << (N-1)) + 1

    sol = []
    for i in range(smallN):
        i2 = mask | (i << 1)
        if divisors[i2] is not None:
            sol.append(i2)
            if len(sol) == J:
                break
    
    proofs = []
    for s in sol:
        base2 = divisors[s]
        p = [str(base2)]
        for base in range(3, 11):
            p.append(change_base(base, base2))
        proofs.append(p)

    check_solution(N, J, sol, proofs)
    
    ans = "\n"
    for i, s in enumerate(sol):
        ans += " ".join([tobinary(s)] + proofs[i]) + "\n"
    return ans
           
def solve_case2(case):
    N, J = case
    assert N > 2 and N % 2 == 0
    halfN = N // 2
    assert 2**(halfN - 2) > J
    mask = 2**(N - 1) + 2**halfN + 2**(halfN - 1) + 1
    divisors = [str(base**halfN + 1) for base in range(2, 11)]
    solutions = []
    for i in range(J):
        sol = mask + i*2*(1 + 2**halfN)
        solutions.append(sol)
    
    check_solution(N, J, solutions, [divisors]*J)

    ans = "\n"
    for i, s in enumerate(solutions):
        ans += " ".join([tobinary(s)] + divisors) + "\n"
    return ans

def check_solution(N, J, sol, proofs):
    assert len(sol) == len(proofs)
    assert len(sol) == J
    assert len(set(sol)) == J
    for i in range(J):
        s, p = sol[i], proofs[i]
        assert len(p) == 9
        bs = tobinary(s)
        for base in range(2, 11):
            bignum = 0
            for i, b in enumerate(bs[::-1]):
                if b == "1":
                    bignum += base**i
            div = int(p[base-2])
            if bignum % div != 0:
                raise Exception("bignum: {}, divisor: {}, sol: {}, base: {}, div2: {}".format(bignum, div, s, base, p[0]))


if __name__ == "__main__":
    instrm = open(sys.argv[1])
    ncases = int(instrm.readline().strip())
    for i in range(ncases):
        case = parse_case(instrm)
        ans = solve_case2(case)
        print("Case #{}: {}".format(i+1, ans), end="")
