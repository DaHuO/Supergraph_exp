#!/usr/bin/env python

def generate_primes(N):
    num_list = [x for x in range(N + 1)]
    for i in range(2, N + 1):
        if num_list[i] == 0:
            continue
        for j in range(i * i, N + 1, i):
            num_list[j] = 0

    primes = []
    is_prime = {}
    for n in num_list:
        if n != 0 and n != 1:
            primes.append(n)
            is_prime[n] = True
        else:
            is_prime[n] = False
    return primes

def get_next_string(x):
    c = 0
    i = len(x) - 1
    new_x = ''
    if x[i] == '0':
        new_x += '1'
    else:
        new_x += '0'
        c = 1
    i -= 1
    while i >= 0:
        new_x += str((int(x[i]) + c) % 2)
        c = (int(x[i]) + c) / 2
        i -= 1

    if c:
        new_x += '1'

    return new_x[::-1] 

def print_jamcoins(N, J, primes):
    x = '00000000000000'
    c = 0

    while c < J:
        div_list = []
        for i in range(2, 11):
            num = int('1' + x + '1', i)
            for k in primes:
                if num % k == 0 and k != num:
                    div_list.append(k)
                    break
        if len(div_list) == 9:
            print '%s %s' % ('1' + x + '1', ' '.join(map(str, div_list)))
            c += 1
        x = get_next_string(x)

if __name__ == '__main__':
    primes = generate_primes(33333335)
    T = int(raw_input())
    for tc in range(1, T + 1):
        N, J = map(int, raw_input().split())
        print 'Case #%d:' % tc
        print_jamcoins(N, J, primes)

