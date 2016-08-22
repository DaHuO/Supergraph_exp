import math
import itertools
inputData = [line.rstrip('\n') for line in open('C-small-attempt0.in', 'r')]
outputList = []


def get_binary_nums(n):
    if n < 2:
        raise ValueError("n must be 2 or bigger")

    for variation in ["".join(item) for item in itertools.product("10", repeat=n-2)]:
        yield '1' + variation + '1'


def find_nontrivial_divisor_for(n):
    if n <= 1:
        return None
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return None


def find_jam_coins(jam_len, jam_amount):
    bins = get_binary_nums(jam_len)
    jam_coins = []
    for binary in bins:
        jam_coin_with_proof = [binary]

        for i in range(2, 11):
            bin_based = int(binary, i)
            nontrivial_divisor = find_nontrivial_divisor_for(bin_based)
            if nontrivial_divisor is None:
                break
            jam_coin_with_proof.append(str(nontrivial_divisor))

        if len(jam_coin_with_proof) == 10:
            jam_coins.append(' '.join(jam_coin_with_proof))
        if len(jam_coins) == jam_amount:
            return jam_coins


for c in range(1, int(inputData[0]) + 1):
    outputList.append('Case #' + str(c) + ':\n')

    jam_len, jam_amount = inputData[c].split(' ')

    for jam_coin in find_jam_coins(int(jam_len), int(jam_amount)):
        outputList.append(jam_coin + '\n')


with open("C-small-attempt0.out", "w") as fw:
    fw.writelines(outputList)