import math

#helper functions
# get the base representation
def base_value(binstring,base):
    total = 0
    power = len(binstring)-1
    for each in binstring:
        if each == '1':
            total += base**power
        power -= 1

    return total

#print base_value("1001", 2) #9
#print base_value("1001", 3) #28

# check for non-prime between bases 2 through 10 and generate the values
def base_nonprime(binstring):
    nonprimes = []
    for i in range(2,11):
        value = base_value(binstring,i)
        if is_prime(value):
            return []
        else:
            nonprimes.append(value)
    return nonprimes
# check if a number is prime
def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True

    sqr_root = int(round(math.sqrt(number)))
    for i in range(2, sqr_root):
        if number % i == 0:
            return False

    return True

#print is_prime(3) # True
#print is_prime(323) # False
#print is_prime(337) # True

# generate non trivial divisors from a list of non prime numbers
def nontriv_divs(nonprimes):
    nontrivs = []
    for np in nonprimes:
        nontrivs.append(get_nontriv_div(np))
    return nontrivs

def get_nontriv_div(number):
    if number > 3:
        sqr_root = int(round(math.sqrt(number)))
        for i in range(3, sqr_root+1):
            if number % i == 0:
                return i
    return None

#print get_nontriv_div(9) #3
#print get_nontriv_div(28) #7
#print get_nontriv_div(65) #5
#print get_nontriv_div(126) #5
#print get_nontriv_div(217) #6
#print get_nontriv_div(344) #31

def generate_coinjam(N, J):
    if N == 2:
        return "11"
    elif N == 3:
        return "111"
    else:
        possible = []
        digit_remain = N - 2
        mid_value = '0' * digit_remain
        possible.append("1" + mid_value + "1")
        for i in range( 2**(len(mid_value)) ):
            mid_value = bin_add(mid_value,'1')
            if len(mid_value) > digit_remain:
                break
            possible.append("1" + mid_value.zfill(digit_remain) + "1")

        # go through all possibility till J
        j = 0
        k = 0
        while j < J and k < len(possible):
            nonprimes = base_nonprime(possible[k])
            if len(nonprimes) > 0:
                nontrivs = nontriv_divs(nonprimes)
                if nontrivs.count(None) == 0:
                    output.write( possible[k] + " " + " ".join(map(str,nontrivs)) +"\n" )
                    j += 1
            k += 1
def bin_add(*args):
    return bin(sum(int(x,2) for x in args))[2:]

filename = 'C-coinjam-small.in.txt'
with open(filename, 'r') as file, open('output_coinjam.txt','w') as output:
    lines = [line for line in file]
    test_cases = int(lines[0])
    for i in range(1, test_cases+1):
        output.write( "Case #%i:\n" %(i) )
        line = lines[1].strip().split(' ')
        N, J = int(line[0]), int(line[1])
        generate_coinjam(N, J)
        
    
