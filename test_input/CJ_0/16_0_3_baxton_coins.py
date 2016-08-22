

import sys


MAX_PRIME = 31 * 31
PRIMES = [2,3,5,7,11,13,17,19,23,29,31]


MULS = [
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],
        [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907],
        [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824],
        [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125],
        [1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336, 13060694016, 78364164096, 470184984576],
        [1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201, 96889010407, 678223072849, 4747561509943],
        [1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592, 68719476736, 549755813888, 4398046511104, 35184372088832],
        [1, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 205891132094649],
        [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000],
       ]



def is_prime(val, divs=None):
    for p in PRIMES:
        if p * p > val:
            break
        if 0 == (val % p):
            if None != divs:
                divs.append(p)
            return False
    return True



def add_primes(val):
    global MAX_PRIME, PRIMES

    if val <= MAX_PRIME:
        return

    MAX_PRIME = val

    p = PRIMES[-1] + 1
    while p * p < val:
        if is_prime(p):
            PRIMES.append(p)
        p += 1
    




def check(val):
    result = [0] * 11
    result[1] = val

    tmp_rep = [0] * 9
    mul_idx = 0
    while val:
        v = val % 2
        val /= 2

        # 2 base
        tmp_rep[0] += v * MULS[0][mul_idx]
        # 3 base
        tmp_rep[1] += v * MULS[1][mul_idx]
        # 4 base
        tmp_rep[2] += v * MULS[2][mul_idx]
        # 5 base
        tmp_rep[3] += v * MULS[3][mul_idx]
        # 6 base
        tmp_rep[4] += v * MULS[4][mul_idx]
        # 7 base
        tmp_rep[5] += v * MULS[5][mul_idx]
        # 8 base
        tmp_rep[6] += v * MULS[6][mul_idx]
        # 9 base
        tmp_rep[7] += v * MULS[7][mul_idx]
        # 10 base
        tmp_rep[8] += v * MULS[8][mul_idx]

        #
        mul_idx += 1

    for i in range(9):
        divs = []
        if not is_prime(tmp_rep[i], divs):
            result[i+2] = divs[0]
        else:
            return result
    result[0] = 1

    return result



    
def solve(t, N, J):
    L = N - 2
    END_NUM = 2 ** L
    mid_num = 0
    RIGHT_MASK = 2 ** (N - 1)
    LEFT_MASK  = 1

    result = ["Case #%d:\n" % t]
    count = 0

    while mid_num < END_NUM and  count < J:

        # prep number
        tmp = RIGHT_MASK | (mid_num << 1) | LEFT_MASK
        add_primes(tmp)

        # check
        res = check(tmp)
        if res[0]:
	    result.append("%s %d %d %d %d %d %d %d %d %d\n" % (bin(res[1])[2:], res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10]))
            count += 1

        # next iteration
        mid_num += 1

    return ''.join(result)


def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        tokens = sys.stdin.readline().strip().split(' ')
        N = int(tokens[0])
	J = int(tokens[1])
        print solve(t+1, N, J)




main()
