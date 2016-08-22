def is_prime(num):
    up_to = int(num**0.5)
    
    if num % 2 == 0:
        return False
    
    for i in range(3, up_to, 2):
        if num % i == 0:
            return False
    return True


def first_factor(num):
    """ assumes num is composite """
    for i in range(2, num):
        if num % i == 0:
            return i

def increment_coin(coin_str):
    b10_int = int("0b"+coin_str, 2)
    b10_int += 1
    return bin(b10_int)[2:]


def coin_str_to_base(coin, base):
    int_result = 0
    index = 0
    for char in reversed(coin):
        if char == '1':
            int_result += (base ** index)
        index += 1
    return int_result


def solve(infile, outfile):
    infile.readline() #reads 1 (there will always be 1 test case)
    coin_length, target = [int(i) for i in infile.readline().strip("\n").split()]
    
    coin = "1" + "0"*(coin_length - 2) + "1"
    valid_coins = []
    
    while target:
        is_valid_coin = True
        for base in range(2, 11):
            if is_valid_coin:
                if is_prime(coin_str_to_base(coin, base)):
                    is_valid_coin = False
        if is_valid_coin:
            valid_coins.append(coin)
            target -= 1
        coin = increment_coin(coin)
        while coin[-1] == '0':
            coin = increment_coin(coin)
    
    outfile.write("Case #1:\n")
    for c in valid_coins:
        to_print = c
        for b in range(2, 11):
            base_num = coin_str_to_base(c, b)
            to_print += " " + str(first_factor(base_num))
        outfile.write(to_print+"\n")


if __name__ == '__main__':
    
    path = 'Data/'
    name='C_test'
    #name='C-small-attempt-0'
    #name='C-large'
    
    infile = open(path+name+'.in', 'r')
    outfile = open(path+name+'.out','w')
    
    solve(infile, outfile)
    infile.close()
    outfile.close()