from math import sqrt, ceil


def gen_coins(current_coin, length, coin_dict, stop):
    if len(coin_dict) < stop:
        if len(current_coin) == length:
            factors = get_factors(current_coin)
            if len(factors) > 0:
                coin_dict[current_coin] = factors
        else:
            if len(current_coin) + 1 < length:
                gen_coins(current_coin + "0", length, coin_dict, stop)
            gen_coins(current_coin + "1", length, coin_dict, stop)


def get_factors(to_factor):
    factors = []
    for base in range(2, 11):
        n = int(to_factor, base)
        current_factor = 2
        while n % current_factor != 0 and current_factor < ceil(sqrt(n)):
            current_factor += 1
        if n % current_factor == 0:
            factors.append(str(current_factor))
        else:
            return []
    return factors

answerFile = open("out.txt", "w")
coins = {}
gen_coins("1", 16, coins, 50)
answerFile.write("Case #1:\n")
count = 0
for coin in coins:
    result = str(coin + " " + " ".join(coins[coin]))
    answerFile.write(result + "\n" if count < 49 else result)
    count += 1
