# from utilities import nonstd
# std = nonstd.IO(in_file='coinjam.in', out_file='coinjam.out')

test_cases = int(input())


def generate_next_coin(coin):
    for i in reversed(range(len(coin)-1)):
        if coin[i] == 0:
            coin[i] = 1
            for j in range(i+1, len(coin)-1):
                coin[j] = 0
            return True
    return False

def interpret_coin(coin, base):
    coin_value = 0
    power = 0
    for i in reversed(range(len(coin))):
        coin_value += coin[i] * (base ** power)
        power += 1
    return coin_value

def get_divisor(coin_value):
    divisor = -1
    i = 2
    while i * i <= coin_value:
        if coin_value % i == 0:
            return i
        i += 1
    return divisor

def get_trivial_divisors(coin):
    divisors = []
    for base in range(2, 11):
        coin_value = interpret_coin(coin, base)
        divisor = get_divisor(coin_value)
        if divisor == -1:
            return -1
        else:
            divisors.append(divisor)
    return divisors



for test_case in range(test_cases):
    temp = input().strip().split()
    coin_length = int(temp[0])
    req_coins = int(temp[1])
    coin = [0 if (i != 0 and i != (coin_length-1)) else 1 for i in range(coin_length)]

    print('Case #' + str(test_case+1) + ':')
    while req_coins > 0:
        trivial_divisors = get_trivial_divisors(coin)
        if trivial_divisors != -1:
            #print(trivial_divisors)
            print("".join([str(digit) for digit in coin]), " ".join([str(divisor) for divisor in trivial_divisors]))
            req_coins -= 1

        if not generate_next_coin(coin):
            break





