import sys
import os
import math

def incrementer(coin) :
    last = len(coin) - 2
    coin[last] += 1
    while last > 1 and coin[last] > 1 :
        coin[last] = 0
        last -= 1
        coin[last] += 1

def value(coin, b) :
    val = 0
    for i in range(N) :
        val = val*b + coin[i]
    return val

def search_divider(val) :
    if val % 2 == 0 :
        return 2
    divider = 3
    max_div = math.sqrt(val)
    while divider <= 100 :
        if val % divider == 0 :
            return divider
        divider += 2
    return 0

def find_coins(N, J, output_file) :
    # Coin
    coin = [0 for i in range(N)]
    coin[0] = 1
    coin[-1] = 1

    nb_found = 0
    while nb_found < J :
        # Coin + dividers
        coin_L = [0 for i in range(10)]
        coin_L[0] = int(''.join(map(str, coin)))
        b = 2
        while b <= 10 :
            val = value(coin, b)
            divider = search_divider(val)
            if divider == 0 :
                b = 2
                incrementer(coin)
                coin_L = [0 for i in range(10)]
                coin_L[0] = int(''.join(map(str, coin)))
            else :
                coin_L[b-1] = divider
                b += 1
        output_file.write(' '.join(map(str, coin_L)) + "\n")
        output_file.flush()
        nb_found += 1
        incrementer(coin)


if (len(sys.argv) < 2) :
    print("No input filename given.", file = sys.stderr)
    sys.exit(1)

input_filename = sys.argv[1]
if (len(sys.argv) > 2) :
    output_filename = sys.argv[2]
else :
    output_filename = os.path.splitext(input_filename)[0] + ".out"

try:
    input_file = open(input_filename, 'r')
except IOError:
    print("Unable to open " + input_filename + " for input.", file = sys.stderr)
    sys.exit(1)

try:
    output_file = open(output_filename, 'w')
except IOError:
    print("Unable to open " + output_filename + " for output.", file = sys.stderr)
    sys.exit(1)

T = int(input_file.readline().rstrip())
enonce = input_file.readline().split()
N = int(enonce[0])
J = int(enonce[1])
output_file.write("Case #1:\n")
find_coins(N, J, output_file)

input_file.close()
output_file.close()
