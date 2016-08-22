

def divisor(num):
    d = 2
    while d * d <= num:
        if num % d == 0:
            return d
        d += 1
    return None


def find(now, N):
    spec = '1{{:0{}b}}1'.format(N - 2)
    while True:
        s = spec.format(now)
        divisors = []
        for radix in range(2, 11, 1):
            num = int(s, radix)
            d = divisor(num)
            if d is None:
                break
            divisors.append(d)
        if len(divisors) == 9:
            return now + 1, s, divisors
        now += 1


def run():
    N, J = map(int, input().split())
    now = 0
    while J > 0:
        now, s, divisors = find(now, N)
        print(s, ' '.join(map(str, divisors)))
        J -= 1


if __name__ == '__main__':
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1))
        run()


                       
