import math

def notPrime(num):
    """ If decimal num is not a prime, return smallest nontrivial divisor
        Otherwise return 0
    """
    if num % 2 == 0: 
        return 2
    divisor = 3   # All numbers are odd
    squareRoot = int(math.sqrt(num))
    while divisor <= squareRoot:
        if num % divisor == 0:  # If true, number is not prime
            return divisor
    	divisor += 2
    return 0 # Number is prime

def Solution():
    t = int(raw_input())  # read a line with a single integer
    N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #1:"

    # length of N
    start = 2**(N-1)
    count = 0
    for i in range(1, start, 2):
        jamcoin = bin(start+i)[2:]
        #print "try jamcoin = ",jamcoin, " (",start+i,")"
        if count == J:        
            break
        if not notPrime(start+i):
            continue
        interpretation = [int(jamcoin, k) for k in range(2,11)]
        #print "interpretation=",interpretation
        divisors = [notPrime(j) for j in interpretation]
        #print "divisors =",divisors
        if 0 in divisors: # is prime
            continue
            
        # found a jamcoin
        print "{} {}".format(jamcoin, " ".join([str(n) for n in divisors]))
        count += 1

if __name__ == "__main__":
    Solution()