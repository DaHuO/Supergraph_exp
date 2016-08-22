
def incr(arr):
    # increment. Or error
    i = len(arr) - 2
    while arr[i] != 0:
        arr[i] = 0
        i -= 1
        if i == 0:
            raise Exception("incremented out of bounds")
    arr[i] = 1

def getVal(arr, base):
    v = 0
    i = len(arr) - 1
    t = 1
    while i >= 0:
        if arr[i] == 1:
            v += t
        t *= base
        i -= 1
    return v

assert getVal([1, 0], 2) == 2
assert getVal([0, 1], 2) == 1
assert getVal([1, 0], 10) == 10
assert getVal([1, 0, 0], 10) == 100

import math
def is_prime(x, limit=.1):
    s = time.time()
    if x == 2 or x == 3: return True, 0
    if x < 2 or x % 2 == 0:
        if x < 2:
            return False, x
        else:
            return False, 2
    if x < 9: return True, 0
    if x % 3 == 0: return False, 3
    f = 5
    r = math.sqrt(x)
    while f <= r:
        if time.time() - s > limit:
            return True, 0
        if x % f == 0:
            return False, f
        if x % (f + 2) == 0:
            return False, f + 2
        f += 6
    return True, 0

cases = int(raw_input())
n, j = (int(x) for x in raw_input().split())

arr = [1] + [0] * (n - 2) + [1]
import time

coins = []
t = 0
i = 0
print "Case #1:"
while len(coins) < j:
    # find a new coin
    c = []
    s = time.time()
    for base in range(2, 11):
        # Find the value of the coin in this base
        v = getVal(arr, base)
        p, f = is_prime(v)
        if p: break
        assert f != 1 and v % f == 0
        c.append(f)
    else:
        coins.append(["".join(str(x) for x in arr)] + c)
        print " ".join(str(x) for x in coins[-1])

    incr(arr)
    t += time.time() - s
    i += 1
