# Return the least factor if a is composite
# Return -1 if a is prime
import math
def leastFactor(a,bound):
    for i in range(2, math.floor(math.sqrt(a))+1):
       if a%i == 0:
           return i
       # Control the value of i so that the algorithm runs faster
       if i>bound:
           break
    return -1

# There are 2**(N-2) choices in total
# extra controls the range of numbers we search.
# For example, when N=6, J=3.
# We have 2**4 = 16384 choices.
# Since 3<2**2, the default is to search 4 numbers.
# extra will increase the range.
# If extra = 1, then search 2**3=8 numbers.
# If extra = 2, then search 2**4=16 numbers.
# 100001 to 111111
def jamcoin(N,J,extra,bound):
    m = 1
    while 2**m <= J:
        m += 1

    # Initialization
    t = m+extra
    cur = [1] + [0]*(N-2) + [1]
    factors = [0 for i in range(9)]
    j = 0
    for i in range(2**t):
        isPrime = False
        s = ''.join(str(e) for e in cur)
        for b in range(2,11):
            f = leastFactor(int(s,b),bound)
            if f==-1:
                isPrime = True
                break
            else:
                factors[b-2] = f
        if isPrime == False:
            print(s, end=' ')
            print(' '.join(str(e) for e in factors))
            j += 1
            if (j==J):
                break
            
        # Increment current (except left digit 1 and right digit 1) by 1
        val = cur[-2] + 1
        if val == 2:
            cur[-2] = 0
            if t >= 2:
                for k in range(t-1):
                    if cur[-(3+k)] == 1:
                        cur[-(3+k)] = 0
                    else:
                        cur[-(3+k)] = 1
                        break
        else:
            cur[-2] = 1


# main function
if __name__ == "__main__":
    T = int(input())
    N, J = map(int, input().split())
    print("Case #%d: " %T)
    jamcoin(N,J,4,1000)
