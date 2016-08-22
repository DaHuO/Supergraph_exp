import math

def get_first_r_jamcoin(digits):
    return list("1" + "0" * (digits - 2) + "1")

"""
Operates on reversed jamcoins.
"""
def next_r_jamcoin(r_jamcoin):
    for i in range(1, len(r_jamcoin)):
        if (r_jamcoin[i] == "1"):
            r_jamcoin[i] = "0"
        else:
            r_jamcoin[i] = "1"
            return r_jamcoin
    return None

def r_jamcoin_to_bin(r_jamcoin):
    bin_string = ""
    for i in range(len(r_jamcoin)):
        bin_string = r_jamcoin[i] + bin_string
    return bin_string
"""
Reversed jamcoin to number.
"""
def r_jamcoin_as_base(r_jamcoin, base):
    my_num = 0
    for i in range(0, len(r_jamcoin)):
        my_num += int(r_jamcoin[i]) * base ** i
    return my_num

def find_divisor(my_num):
    for i in range(2, int(math.sqrt(my_num)) + 1):
        quotient = my_num / i
        remainder = my_num - quotient * i
        if remainder == 0:
            return i
    return -1

def get_divisor_list(r_jamcoin):
    
    # Test divisibility of all bases
    failed = False
    divisibility = [None] * 9
    for base in range(2, 10 + 1):

        divisor = find_divisor(r_jamcoin_as_base(r_jamcoin, base))

        if divisor == -1:
            failed = True
            break

        divisibility[base - 2] = str(divisor)
        
    if (failed == True):
        return None
    else:
        return divisibility

g = open("C-small-attempt0.out", "w")
jam_coins = 0
g.write("Case #1:\n")
my_r_jamcoin = get_first_r_jamcoin(16)
while (jam_coins < 50):

    divisor_list = get_divisor_list(my_r_jamcoin)
    if (divisor_list != None):
        jam_coins += 1
        message = r_jamcoin_to_bin(my_r_jamcoin) + " " + " ".join(divisor_list)
        print jam_coins, message
        g.write(message + "\n")

    my_r_jamcoin = next_r_jamcoin(my_r_jamcoin)
    if (my_r_jamcoin == None):
        print "Program ended prematurely."
        break

g.close()
