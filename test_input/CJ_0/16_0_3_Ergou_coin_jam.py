def factorize(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return 0


def coins(N, J):
    template = '1{0:0%db}1' % (N - 2)
    i = 0
    ret = []
    while len(ret) < J:
        s = template.format(i)
        factors = []
        for base in range(2, 11):
            f = factorize(int(s, base))
            if f > 0:
                factors.append(str(f))
            else:
                break
        else:
            ret.append([s] + factors)
        i += 1
    return ret

if __name__ == '__main__':
    with open('C-small-attempt0.in') as fin, open('output', 'w') as fout:
        fin.readline()
        N, J = [int(i) for i in fin.readline().split()]
        fout.write('Case #1:\n')
        for i in coins(N, J):
            fout.write(' '.join(i) + '\n')