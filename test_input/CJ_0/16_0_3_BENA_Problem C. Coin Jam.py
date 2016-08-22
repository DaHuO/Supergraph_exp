


def highest_prime_factor(n):
    if isprime(n):
        return n
    for x in xrange(2,int(n ** 0.5) + 1):
        if not n % x:
            return highest_prime_factor(n/x)

def isprime(n):
    if n == 2 : return True
    for x in xrange(3 ,int(n ** 0.5) + 1, 2):
        if not n % x:
            return False
    return True


def getBinList(i, l):
    r = '{0:0b}'.format(i)
    while len(r) != l:
        r = '0' + r
    return list(r)

def solve(n, j):
    nums = []
    for i in range(n):
        nums.append(0)
    nums[0] = '1'
    nums[n-1] = '1'
    l = n - 2

    rstList = []

    for i in range(2**l):
        # decimal to binary
        b = getBinList(i, l)
        #print i, b
        for idx in range(len(b)):
            nums[idx+1] = str(b[idx])


        ## not prime all
        for base in range(2, 11):
            dec = int(''.join(nums), base)

            prime = isprime(dec)

            #print nums, base, dec, prime

            if prime:
                print "It is PRIME", nums, base, dec, prime
                break

        if prime:
            continue

        rowList = []
        rowList.append(''.join(nums))
        for base in range(2, 11):
            dec = int(''.join(nums), base)
            highest = highest_prime_factor(dec)
            rowList.append(highest)

        rstList.append(rowList)

        if len(rstList) == j:
            return rstList
    return rstList

def main():
    #inputFile = "A-large.in"
    #inputFile = "B-small-attempt0 (1).in"
    #inputFile = "B-large.in"
    #inputFile = "C-small-practice.in"
    inputFile = "C-small-attempt0.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        #n = [int(x) for x in inpf.readline().strip().split(' ')]
        n, j = [int(x) for x in inpf.readline().strip().split(' ')]
        #s = inpf.readline()
        rst = solve(n, j)

        result = 'Case #{}:\n'.format(case+1)
        print result,
        outf.write(result)

        for r in rst:
            result = ' '.join([str(x) for x in r]) + '\n'
            print result,
            outf.write(result)

        #print s,
        #print result,
        #outf.write(result)
    inpf.close()
    outf.close()

def main2():
    rst = solve(6,3)
    print rst,


if __name__ == "__main__":
    main()
    #main2()




