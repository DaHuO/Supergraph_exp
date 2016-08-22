import itertools

cases = int(input())
def prime_factor(number):
    i = 2
    n = number
    # print number
    while i!=n:
        if n%i==0:
            return i
        i += 1
    return None

for i in range(cases):
    print("Case #%d:" % (i+1,))
    # n = 32
    # j = 500
    n, j = map(int, raw_input().split())
    for nz in range(2, n, 2):
        for pos in itertools.combinations(range(1, n-1), nz):
            num = [1] * n
            for p in pos:
                num[p] = 0
            x = ''.join(map(str, num))
            if j != 0:
                coins = [prime_factor(int(x, base)) for base in range(2,11)]
                if None not in coins:
                    print(x + " " + ' '.join(map(str, coins)))
                    # print x, pos
                    j -= 1
            else:
                break
        if j==0:
            break