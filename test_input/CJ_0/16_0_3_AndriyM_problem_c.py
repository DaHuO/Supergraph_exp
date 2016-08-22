
def get_divisor(n):
    for i in range(2, min(n, 5000)):
        if n%i ==0:
            return i

    return None


def generate_potential_jamcoins(N):
    for i in range(2**(N-1) + 1, 2**N):
        if i % 2 == 1:
            yield '{0:b}'.format(i)


def test_jamcoin(jamcoin):
    divisors = []
    for base in range(2, 11):
        num = int(jamcoin, base)
        div = get_divisor(num)
        if div is None:
            return None
        else:
            divisors.append(div)
    return divisors


def generate_jamcoins(J, N):
    res = []
    for pot_j in generate_potential_jamcoins(N):
        if len(res) >= J:
            return res
        div_list = test_jamcoin(pot_j)
        if div_list is not None:
            res.append((pot_j, div_list))
    return res


FILE_NAME = 'c_test'

if __name__ == '__main__':
    with open(FILE_NAME + '.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open(FILE_NAME + '.out', 'w') as out:
        for i in range(1, T + 1):
            N, J = map(int, lines[i].split(' '))
            out.write('Case #%d:\n' % i)
            for j_coins in generate_jamcoins(J, N):
                out.write(j_coins[0] + ' ' + ' '.join(map(str, j_coins[1])) + '\n')
