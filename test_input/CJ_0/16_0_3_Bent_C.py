import random

def Fermat(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(10):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False

def getDivisor(number):
    i = 1
    while i < number:
        i += 1
        if (number%i == 0):
            return i
    return 1

def toBase(bits, base):
    res = 0
    for i in range(16):
        res += int(bits[15-i]) * pow(base, i)
    return res

def solve():
    target = open("C-small-attempt0.out.txt", 'w')
    target.write("Case #1:\n")
    N = 16
    J = 50
    for i in range(pow(2, N-1)+1, pow(2, N)):
        if (J == 0):
            break
        divisors = list()
        bits = '{0:16b}'.format(i)
        if (bits[-1] == '0'):
            continue
        for b in range(2,11):
            res = 0
            for j in range(16):
                res += int(bits[15-j]) * pow(b, j)
            if (Fermat(res)):
                break
            divisors.append(getDivisor(res))
        if (len(divisors) != 9):
            continue
        target.write(bits)
        for j in range(9):
            target.write(" ")
            target.write(str(divisors[j]))
        target.write("\n")
        J -= 1
