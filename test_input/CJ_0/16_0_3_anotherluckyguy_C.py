import itertools

lines = open('input.txt').readlines()
tests = lines[0]
lines.remove(lines[0])
output = open('out.txt', 'w')
lines = [i.strip() for i in lines]

jamcoins = set()
print(lines)


def get_coins(N):
    for string in map(''.join, itertools.product('01', repeat=N - 2)):
        jamcoins.add(int('1' + string + '1'))


def is_jamcoin(jamc):
    divisors = []
    for i in range(2, 11):
        for d in range(2, jamc // 2):
            if d > 100:
                break
            if int(str(jamc), i) % d == 0:
                # print(d, i)
                divisors.append(d)
                break
    if len(divisors) == 9:
        return divisors
    return False


a = 1
b = 0
for it in range(int(tests)):
    # N, J = it.split()
    N = 32
    J = 500
    output.write('Case #{}:\n'.format(a))
    for string in map(''.join, itertools.product('01', repeat=N - 2)):
        jamcoin = int('1' + string + '1')
        if not is_jamcoin(jamcoin):
            continue
        b += 1
        print(jamcoin, ' '.join([str(i) for i in is_jamcoin(jamcoin)]))
        output.write(str(jamcoin) + ' ' + ' '.join([str(i) for i in is_jamcoin(jamcoin)]) + '\n')
        if b == J:
            break

    a += 1
