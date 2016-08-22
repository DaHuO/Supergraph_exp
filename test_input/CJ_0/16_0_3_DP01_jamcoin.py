"""
Rules
=====

* The pattern will always be in alternate fashion, ie, TFTFTFTF. If it isn't, it can be reduced to this pattern.
* Since it's in an alternate pattern, the fastest solution will always be the one that will be acheieved by recursively flipping the first bit and reducing the pattern.
"""

_name = "A"

# Load the file in a list
with open("{}.in".format(_name)) as f:
    data_set = [line.rstrip() for line in f]

# Remove the first entry since we don't really need it.
no_of_tests = data_set.pop(0)

max_size = int(data_set[0][0:2])
required_coins = int(data_set[0][3:5])
current_test_no = 1

def create_jamcoin(_last=None):
    """
    Rules
    =====
    * Digits can only be 1 or 0;
    * First and last digit should be zero;
    * It shouldn't be a prime number in base 2 to 10;
    """

    _base_values = []
    _ntd = []

    if _last:
        coin_value = str(_last[1:max_size-1])
        temp_coin = int(coin_value, 2) + int("1", 2)
        temp_coin = bin(temp_coin)[2:].zfill(max_size - 2)

        if len(temp_coin) > max_size - 2:
            return "Max allowed length reached"
    else:
        temp_coin = "0" * (max_size - 2)

    # Append "1" in the start and end of the temp_coin to fulfill rules.
    unverified_coin = "1" + temp_coin + "1"

    for i in range(2, 11):
        value = check_for_prime(unverified_coin, i)

        if value:
            _base_values.append(value)
        else:
            _base_values = []
            break

    # Return back to the main loop if one of the bases is prime
    if not _base_values:
        return False, unverified_coin
    
    for i in _base_values:
        _ntd.append(non_trivial_divisor(i))

    return _ntd, unverified_coin

def check_for_prime(jamcoin, base):
    """
    Check if the provided jamcoin is a prime number or not.
    If the provided number is not prime, it returns the value, otherwise it returns False.

    jamecoin: The value of the jamcoin.
    base: The base it needs to be checked in.
    """

    value = int(jamcoin, base)
    last_value = int(str(value)[-1])

    # Check if the last value is divisible by 2 or is 5
    if last_value % 2 == 0 or last_value == 5:
        return value

    # 0 and 1 are not primes
    if value < 2:
        return value
 
    # 2 is the only even prime number
    if value == 2: 
        return False
 
    if not value & 1:
        return value
 
    for x in xrange(3, int(value**0.5)+1, 2):
        if value % x == 0:
            return value
    return False

def non_trivial_divisor(v):
    """
    Returns the lowest number the provided value can be divided by
    """

    counter = 3
    _loop = True

    if v % 2 == 0:
        return 2

    while _loop:
        if v % counter == 0:
            return counter
        else:
            counter += 2

def find_all_jamcoin():
    _last_coin = None
    current_coin_no = 0

    with open("{}.out".format(_name), 'a') as f:
        f.write("Case #{0}:\n".format(current_test_no))

    # Main loop for finding genuine jam coins
    while current_coin_no < required_coins:
        _check = False

        if not _last_coin:
            _check, _last_coin = create_jamcoin()
        else:
            _check, _last_coin = create_jamcoin(_last_coin)

            # If the last coin isn't what we want, loop until we found one.
            while not _check:
                _check, _last_coin = create_jamcoin(_last_coin)

        current_coin_no += 1

        with open("{}.out".format(_name), 'a') as f:
            f.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(_last_coin, *_check))

find_all_jamcoin()
