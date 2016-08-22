import binascii
import math
import os
import struct

print "Case #1:"

coin_length = 32
coin_cnt = 500

coin_num = 0
used = []
while(coin_num < coin_cnt):

    coin = struct.unpack("<L", os.urandom(4))[0]
    x = coin
    
    mask = 0
    for i in range(0, coin_length):
        mask = (mask << 1) | 1
    coin = coin & mask

    mask = 1
    for i in range(0, coin_length - 1):
        mask = mask << 1
    mask = mask | 1
    coin = coin | mask

    if coin in used:
        continue
    used.append(coin)

    coin_as_string = bin(coin)[2:]
    output = coin_as_string

    candidate_good = True
    base = 2
    while(candidate_good and base <= 10):
        coin_value = int(coin_as_string, base)

        i = 2
        i_limit = int(math.sqrt(coin_value)) + 1
        i_limit = (i_limit, 1000000)[i_limit >= 1000000]
        base_good = False
        while(not base_good and i <= i_limit):
            base_good = (False, True)[coin_value % i == 0]
            i += (1, 0)[base_good]

        if base_good: 
            output += " %d" % (i)
        else:
            candidate_good = False
        base += 1

    if candidate_good:
        print output
        coin_num += 1