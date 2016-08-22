def is_prime(n):
    b = 2
    while b * b <= n:
        if n % b == 0:
            return False
        b += 1
    return True


def div(n):
    b = 2
    while b * b <= n:
        if n % b == 0:
            return b
        b += 1


t = int(input())
for i in range(1, t+1):
    print("Case #", i, ": ", sep='')
    n, j = map(int, input().split())
    cnt = 0
    for i in range(2**14):
        if cnt == j:
            break
        s = '1' + '0' * (n - 2 - len(bin(i)[2:])) + bin(i)[2:] + '1'
        f = False
        for i in range(2, 11):
            if is_prime(int(s, i)):
                f = True
                break
        if not f:
            cnt += 1
            print(s, end=' ')
            for i in range(2, 11):
                print(div(int(s, i)), end=' ')
            print()