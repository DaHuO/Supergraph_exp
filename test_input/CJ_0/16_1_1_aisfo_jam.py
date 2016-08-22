from collections import deque
from heapq import heappush,heappop

import numpy as np

from math import sqrt


t = int(input())


for case in range(1,t+1):

    #input().split(' ')

    S = input()

    result = S[0]

    for i in range(1,len(S)):
        ch = S[i]
        if ord(ch) < ord(result[0]):
            result = result + ch
        else:
            result = ch + result

    print("Case #{0}: {1}".format(case, result))





