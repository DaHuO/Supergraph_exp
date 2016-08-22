import math

f = open('test.in', 'r')
output = open('test.out', 'w')
C = int(f.readline())

def min_divisor(x):
    if x < 2:
        return True
    for y in range(2, 10000):
        if x % y == 0:
            return y
    return x

def find_N_jamcoins(N, J):
    jamcoins = []
    num = int('1' + '0' * (N - 2) + '1', 2)
    while J > 0:
        jamcoin = format(num, 'b')
        result = is_jamcoins(jamcoin)
        if result != None:
            output.write(str(jamcoin) + " ")
            output.write(" ".join([str(divisor) for divisor in result]))
            output.write("\n")
            jamcoins.append(jamcoin)
            J -= 1
        num += 2
    return jamcoins

def is_jamcoins(bin):
    divisors = []
    for base in range(2, 11):
        num = int(bin, base)
        min_div = min_divisor(num)
        if min_div == num:
            return None
        else:
            divisors.append(min_div)
    return divisors

if __name__ == "__main__":
    for i in range(0, C):
        line = f.readline().rstrip('\n').split()
        N = int(line[0])
        J = int(line[1])
        output.write("Case #" + str(i + 1) + ":\n")
        find_N_jamcoins(N,J)