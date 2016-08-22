from __future__ import print_function
import sys

coins = set()
J = 500

def dbg(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)

print("Case #1:")
for line in sys.stdin:
    coin, rest = line.strip().split(None, 1)
    nums = [int(coin, base=b) for b in range(2, 11)]
    factors = [int(x) for x in rest.split()]
    #print('')
    #print(coin)
    #print(nums)
    #print(factors)
    if not (coin[0] == coin[-1] == '1'):
        raise AssertionError
    if not all(n%f==0 for n, f in zip(nums, factors)):
        dbg(coin)
        dbg(nums)
        dbg(factors)
        raise AssertionError
    if coin in coins:
        dbg('Double coin!!')
        continue

    coins.add(coin)
    sys.stdout.write(line)

    if len(coins) == J:
        break

dbg(coins)
dbg(len(coins))
