from __future__ import print_function

from random import random
from itertools import count

for i in count():
    #N = 16
    N = 32
    coin = ''.join(('1' if random() < .5 else '0') for _ in range(N-2))
    coin = '1' + coin + '1'
    assert(len(coin) == N)

    try:
        print(coin, ' '.join(str(int(coin, base=b)) for b in range(2, 11)))
    except IOError:
        break
    #if i > 100:
    #    break
