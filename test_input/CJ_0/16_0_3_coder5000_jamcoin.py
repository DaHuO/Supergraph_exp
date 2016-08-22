import itertools

def main():
    t = int(input())
    for i in range(1, t + 1):
        n,j = raw_input().split(' ')
        jam_coins(i, int(n), int(j))

def coin_numbers(coin):
    for base in range(2, 11):
        yield int(coin, base)

def divisible_by(number):
    for i in range(2, 20):
        if number % i == 0:
            return i
    return -1

def jam_coins(index, n, j):
    print('Case #1:')
    jam_coins = []
    generate_coin = itertools.product("01", repeat=n-2)
    while len(jam_coins) != j:
        coin = "".join(generate_coin.next())
        coin = '1' + coin + '1'

        proof_array = []
        for number in coin_numbers(coin):
            proof = divisible_by(number)
            #reset
            if proof == -1:
                proof_array=[]
                break
            else:
                proof_array.append(proof)

        if proof_array:
            jam_coins.append(coin)
            print(coin +  ' '  +  ' '.join(str(a) for a in proof_array))


if __name__ == "__main__":
    main()
