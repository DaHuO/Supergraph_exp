import math

def get_divisor(n):
    """
        Mersenne prime implementation, I modify it to return 0 if n is prime or the divisor otherwise
        http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
    """
    if n == 2 or n == 3:
        return 0

    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2
    while i * i <= n:
        # I am not interested in divisors big than this, I will asssume it prime and drop it
        if i>100000:
            break
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return 0


def check_number( numstr):
    """
    :param numstr: the number string as 1000110
    :return: list of divisors if jimcoin else [0]
    """
    N= len(numstr)
    divisors = []
    for i in xrange(2,11):
        val=sum([int(numstr[N-j-1]) * int(math.pow(i,j)) for j in xrange(N)])
        div = get_divisor(val)
        if div == 0:
            return [0]
        divisors.append(div)
    return  divisors

def solve(N,J):
    """
    :param N: Number of digits in the Jamcoin
    :param J: Number of jamcoins required
    :return: collection (dict) as 'number i.e. 1001':[list of divisors]
    """
    results ={}
    # generator to generate posssible jamcoins in sequences
    numbers_gen = ('1'+format(i, '0'+str(N-2)+'b')+'1' for i in xrange(int(math.pow(2,N-2))))
    for b in numbers_gen:
        res = check_number(b)
        if res[0] != 0:
            results[b] = res
            if len(results.keys())>=J:
                break
    return results


T=int(raw_input())
for i in xrange(T):
    N,J = (int(s) for s in raw_input().split(' '))
    res = solve(N,J)

    print ("Case #%d:"%(i+1))
    for k in res:
        divstr = [str(d) for d in res[k]]
        print( k+" "+" ".join(divstr))
