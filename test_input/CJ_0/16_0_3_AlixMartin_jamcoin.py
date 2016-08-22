FILENAME = 'test.in'


def load_primes():
    primes = set()
    with open('primes.txt') as f:
        for line in f:
            n = int(line.strip())
            primes.add(n)
            if n > 100001:
                break
    print(len(primes), 'primes loaded')
    return primes


PRIMES = load_primes()

def leftpad(s, n):
    while(len(s) < n):
        s = '0' + s
    return s


def interpretations(s):
    r = []
    for b in range(2, 11):
        r.append(int(s, b))
    return r


def divisors(s):
    r = []
    for n in interpretations(s):
        for p in PRIMES:
            try:
                if n % p == 0:
                    r.append(p)
                    break
            except TypeError:
                print('s', s, 'n', n,'p', p)
                exit(0)
    return r
    #return ' '.join(map(str, r))


def gen(N, J, g):
    count = 0
    for i in range(2 ** (N-2)):
        s = '1' + leftpad("{0:b}".format(i), N-2) + '1'
        if len(set(interpretations(s)).intersection(PRIMES)) > 0:
            continue
            #print(s, interpretations(s), set(interpretations(s)).intersection(PRIMES))
        if len(divisors(s)) < 9:
            continue
        print (s, ' '.join(map(str, divisors(s))))
        g.write(s + ' ' + ' '.join(map(str, divisors(s))))
        g.write('\n')
        count += 1
        if count >= J:
            return




def main():
    with open('test.out', 'w') as g:
        with open(FILENAME) as input:
            T = int(input.readline())
            for t in range(T):
                answer_str = 'Case #{}: '.format(t + 1)
                print(answer_str)
                N, J = map(int, input.readline().strip().split())
                g.write(answer_str)
                g.write('\n')
                gen(N, J, g)



if __name__ == '__main__':
    main()