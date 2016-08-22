def is_prime(x):
    for i in xrange(2, int(x**0.5) + 1):
        if x % i == 0:
            return i
    return True

def check_jamcoin(string):
    divisor = []
    for i in xrange(2, 11):
        c = is_prime(int(string, i))
        if c != True:
            divisor.append(str(c))
        else:
            return False
    return ' '.join(divisor)

if __name__ == '__main__':
    n = 32
    j = 500
    i = 0
    print 'Case #1:'
    counter = 0
    while counter != j:
        x = check_jamcoin('1{:030b}1'.format(i))
        if x:
            counter += 1
            print '%s %s' % ('1{:030b}1'.format(i), x)
        i += 1