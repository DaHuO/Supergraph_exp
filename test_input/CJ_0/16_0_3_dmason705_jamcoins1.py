from numpy import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_divisor(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return i


def getjamcoins(lengthN,numcoinsJ):

    length=lengthN

    num=2**length-1
    coin = format(num,'06b')
    jamcoins=[]
    divisorses=[]

    failsafe=0
    while len(jamcoins)<numcoinsJ:
        failsafe+=1
        if failsafe > 1000:
            # print "FAIL"
            break
        reps=[int(coin,i) for i in range(2,10+1)]
        if coin[0]=='1' and coin[-1]=='1':
            if not any([is_prime(rep) for rep in reps]):
                divisors=[get_divisor(rep) for rep in reps]
                # print coin+" is a good jamcoin!"
                # print "     it's representations are"+str([str(rep)+'  ' for rep in reps])
                # print "       which have divisors"+str([str(div)+'  ' for div in divisors])
                jamcoins.append(coin)
                divisorses.append(divisors)
        num-=1
        coin=format(num,'06b')

    return jamcoins,divisorses



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    # print num
    jamcoins,divisorses = getjamcoins(N,J)
    print "Case #{}:".format(i)
    for k in range(len(jamcoins)):
        print jamcoins[k]+' '+' '.join([str(div) for div in divisorses[k]])
  # check out .format's specification for more formatting options