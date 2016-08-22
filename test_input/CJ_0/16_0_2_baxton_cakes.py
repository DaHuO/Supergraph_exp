

import sys


HAPPY = 1
FLAT  = 0
NOVAL = -1



def init(stack):
    N = len(stack)
    count = 0
    result = [NOVAL] * N
    for i in range(N):
        result[i] = int(stack[i] == "+")
        count += result[i]
    return result, count



def next_cake(stack, beg, c):
    N = len(stack)
    while beg < N and stack[beg] != c:
        beg += 1
    return beg


def solve(stack):
    stack, count = init(stack) 
    flips = 0

    N = len(stack)
    beg = 0

    if FLAT == stack[beg]:
        beg = next_cake(stack, beg+1, HAPPY)
        flips += 1
        if beg >= N:
            return flips

    while beg < N:
        beg = next_cake(stack, beg, FLAT)
        if beg >= N:
            return flips
        beg = next_cake(stack, beg, HAPPY)
        flips += 2
        if beg >= N:
            return flips

    return flips
    


def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        stack = sys.stdin.readline().strip()
        print "Case #%d: %d" % (t+1, solve(stack))




main()
