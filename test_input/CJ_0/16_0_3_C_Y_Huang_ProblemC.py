import math


def solve(num: str) -> []:
    ret = []
    for base in range(2, 11):
        n = int(num, base=base)
        divisor = get_divisor(n)
        ret.append(divisor)
        if not divisor:
            break
    return ret


# n: decimal
def get_divisor(n: int) -> int:
    if n == 2:
        return 2
    if n % 2 == 0: # even
        return 2

    to = math.floor(math.pow(n, 0.5))+1
    for x in range(3, to, 2):
        if n % x == 0:
            return x
    return 0


def populate_jam_string(len: int) -> []:
    ret = []
    from_ = int(math.pow(2, len-1))+1
    to_ = int(math.pow(2, len))
    for n in range(from_, to_, 2):
        ret.append(str(bin(n))[2:])
    return ret

if __name__ == '__main__':

    input() # kCase
    line = input()
    N_, J_ = line.split(' ')
    N = int(N_)
    J = int(J_)

    print('Case #1:')
    p = (populate_jam_string(N))
    count = J
    for n in p:
        if not count:
            break
        ans = solve(n)
        if ans[-1] != 0:
            count -= 1
            print('%s' %n, end='')
            for a in ans:
                print(' %d' %a, end='')
            print()