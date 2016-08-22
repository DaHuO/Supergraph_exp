import math
def main():
    cases = int(input())
    for i in range(cases):
        print("Case #"+str(i+1)+":")
        args = input().split()
        N = int(args[0])
        J = int(args[1])
        iterate_bin(N,J)
def isPrime(num):
    if(num % 2 == 0 and num != 2):
        return 2
    for i in range(3, math.ceil(math.sqrt(num)),2):
        if(num % i == 0):
            return i
    return None
def iterate_bin(N,J):
    found = 0
    for i in range(int("1"*(N-2),2)):
        current = "1"+(bin(i)[2:]).zfill(N-2)+"1"
        factors = [0,0,0,0,0,0,0,0,0]
        prime = False
        for j in range(2,11):
            factor = isPrime(int(current,j))
            if(factor):
                factors[j-2] = factor
            else:
                prime = True
                break
        if not prime:
            factorString = ""
            for factor in factors:
                factorString += " " + str(factor)
            print(current+factorString)
            found += 1
            if(found == J):
                break
main()