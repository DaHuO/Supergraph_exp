import random
import primefac
OUTPUT = 'quite-small-output.txt'
def gen_jamcoin(length):
    return ''.join(['1'] + [random.choice(['0', '1']) for x in range(length-2)] + ['1'])

def gen_all_jamcoins(length, num_coins):
    jamcoins = set()
    while(len(jamcoins) < num_coins):
        potential_coin = gen_jamcoin(length)
        if potential_coin not in jamcoins:
            potential_result = test_num(potential_coin)
            if potential_result:
                jamcoins.add(potential_coin)
                write(potential_coin, potential_result)
                 
def test_num(potential_coin):
    proofs = []
    for x in range(2, 11):
        coin_in_base = int(potential_coin, x)
        if primefac.isprime(coin_in_base):
            return []
        else:
            if coin_in_base > 2**17:
                proofs.append(primefac.ecm(coin_in_base))
            else:
                proofs.append(primefac.pollardRho_brent(coin_in_base))
    return proofs

def write(potential_coin, potential_result):
    with open(OUTPUT, 'a') as w:
        w.write(potential_coin)
        w.write(" ")
        w.write(" ".join([str(x) for x in potential_result]))
        w.write("\n")

gen_all_jamcoins(16, 50)
