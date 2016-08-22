import sys

def get_factor(n):
    if n == 1:
        return False
    x = 2
    while x * x <= n:
        if n % x == 0:
            return x
        x += 1
    return -1

def brute(l):
    cnt = 1
    for mask in range(2 ** (l - 1), 2 ** l):
        if mask % 2 == 0:
            continue
        s = bin(mask)[2:]
        fact = [0 for i in range(2, 11)]
        for base in range(2, 11):
            num = 0
            for i in range(len(s)):
                num = num * base + int(s[i])
            f = get_factor(num)
            if f == -1:
                break
            else:
                fact[base - 2] = f
        else:
            print(cnt, file = sys.stderr)
            print(s, end = ' ')
            for i in range(len(fact)):
                print(fact[i], end = ' ')
            print()
            cnt += 1
            if cnt > 50:
                break

def main():
    print('Case #1:')
    brute(16)

if __name__ == '__main__':
    main()


