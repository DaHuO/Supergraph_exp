#!/usr/local/bin/python3
import numpy as np

# c = int(input())
c = 1
# n, j = [int(item) for item in input().split()]
n, j = 16, 50


def check_not_prime(v):
    results = []
    for i in range(2, 11):
        remain_check = np.array([2] + list(range(3, int(np.sqrt(int(v, i))) + 1, 2)))
        remainders = np.remainder(int(v, i), remain_check)
        if np.sum(remainders == 0) == 0:
            return (False, False)
        results.append(str(remain_check[np.where(remainders == 0)[0][0]]))
    return (v, results)

ll = []
for i in range(2**(n - 2)):
    target = "1" + (("0" * n) + bin(i)[2:])[2 - n:] + "1"
    rr = check_not_prime(target)
    if rr[0]:
        ll.append(rr)
    if len(ll) == j:
        break

print ("Case #1:")
for l in ll:
    print_item = [l[0]] + l[1]
    print (" ".join(print_item))
