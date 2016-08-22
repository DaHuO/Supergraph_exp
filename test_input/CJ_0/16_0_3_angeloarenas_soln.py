import math

def read_integers(filename):
    with open(filename) as f:
        return map(int, f)


def convert_to_base(num, base):
    output = ''
    while num >= base:
        mod = num % base
        num = num / base
        output += str(mod)
    if num > 0:
        output += str(num)
    return int(output[::-1])

def check_prime(num):
    is_prime = True
    x = 2
    while x <= int(math.sqrt(num)):
        if int(num/x) == float(num)/float(x):
            is_prime = False
            break
        x+=1
    if (is_prime):
        return 0
    else:
        return x

#MAIN PROGRAM
#usage of int(s,b) to convert s to base 10
data = read_integers('data.in')
t = data[0]
n = data[1]
j = data[2]

jamcoins = []
i = 1

print 'Case #1:'
while len(jamcoins) < j:
    #generate jamcoin
    bool_ctr = str(convert_to_base(i, 2))
    jcoin = '1'
    for k in range(0, n-len(bool_ctr)-2):
        jcoin += '0'
    jcoin += bool_ctr
    jcoin += '1'
    i+=1

    is_jamcoin = True
    divisors = []
    for k in range(2, 11):
        conv = int(str(jcoin), k)
        divisors.append(check_prime(conv))
        if divisors[k-2] == 0:
            is_jamcoin = False
            break

    if is_jamcoin:
        jamcoins.append(jcoin)
        print jcoin,
        for x in divisors:
            print x,
        print
