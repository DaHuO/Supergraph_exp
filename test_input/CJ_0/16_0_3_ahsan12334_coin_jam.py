# Google Code Jam 2016
# Qualification Round
# Coin Jam

from math import sqrt, floor

def get_base_number(n):
    to_return = []
    for i in range(2, 11):
        to_return.append(int(str(n), i))
    return to_return

def next_coin(jam_coin):
    jam_coin = int(bin(int(str(jam_coin), 2) + 1)[2:])
    return jam_coin

def get_divisor(n):
    # If n is even
    if n % 2 == 0:
        return 2
    else:
        biggest_possible = int(floor(sqrt(n)))
        for d in range(3, biggest_possible + 1, 2):
            if n % d == 0:
                return d
            elif d >= biggest_possible:
                return -1
        return -1
if __name__ == "__main__":
    input_file = open('test.txt', 'r')
    N, J = [int(x) for x in input_file.read().split('\n')[1].split() if x != '']
    input_file.close()

    # Make the first jam_coin
    jam_coin = '1'
    for i in range(1, N):
        jam_coin += '0'
    jam_coin = int(jam_coin)


    with open('output.txt', 'w') as f:
        f.write('Case #1:\n')
        j = 0
        while(j < J):
            if str(jam_coin)[len(str(jam_coin))-1] == '0':
                jam_coin = next_coin(jam_coin)


            bases = get_base_number(jam_coin)
            divisors = [get_divisor(n) for n in bases]
            if -1 in divisors:
                jam_coin = next_coin(jam_coin)
            else:
                # Find Divisors
                f.write(str(jam_coin))
                for d in divisors:
                    f.write(' ' + str(d))
                f.write('\n')
                j += 1
                jam_coin = next_coin(jam_coin)