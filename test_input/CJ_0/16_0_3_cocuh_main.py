import subprocess as sp
_is_prime = {}

def get_divisor(curr) -> (bool, int):
    if curr not in _is_prime:
        divisor = list(map(int, sp.check_output(['factor', '{}'.format(curr)]).decode('UTF-8')\
                [len('{}: '.format(curr)):-1].split(' ')))
        res = len(divisor) == 1
        _is_prime[curr] = (res, divisor[0])
    return _is_prime[curr]

def gen(bit) -> str:
    for i in range(2**(bit-2)):
        res = '1'+ bin(i)[2:].rjust(bit-2,'0')+'1'
        yield res

def gen_jamcoin(N, J):
    num = 0
    for res in gen(N):
        interpretation = [int(res, base=base)for base in range(2,11)]
        divisor = [get_divisor(x) for x in interpretation]
        if any(map(lambda t:t[0], divisor)):
            continue
        output = "{} {}".format(res, ' '.join(map(lambda t:str(t[1]),divisor)))
        yield res, output

def test(N, J):
    for _, jc in zip(range(J), gen_jamcoin(N,J)):
        _, output = jc
        print(output)

def main():
    test_num = int(input())
    for i in range(test_num):
        N,J = map(int, input().split(' '))
        print("Case #1:")
        test(N,J)

if __name__ == '__main__':
    main()
