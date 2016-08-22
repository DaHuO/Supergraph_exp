
def revers(s):
    first = s[0]
    if first == '-':
        otherSide = '+'
    else:
        otherSide = '-'

    for i in range(len(s)):
        if s[i] == first:
            s[i] = otherSide
        else:
            return s
    return s


def isBaked(s):
    for one in s:
        if one == '-' :
            return False
    return True

def solve(s):
    n = 0
    while True:
        rst = isBaked(s)
        if rst == True:
            return n
        else:
            revers(s)
            n = n+1
    return n

def main():
    #inputFile = "B-small-attempt0.in"
    #inputFile = "A-large.in"
    #inputFile = "B-small-practice.in"
    #inputFile = "B-small-attempt0 (1).in"
    inputFile = "B-large.in"
    
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        #n = [int(x) for x in inpf.readline().strip().split(' ')]
        s = inpf.readline()
        rst = solve(list(s.strip()))

        result = 'Case #{}: {}\n'.format(case+1,  rst)

        #print s,
        print result,
        outf.write(result)
    inpf.close()
    outf.close()

def main2():
    case = 0
    n = 1256
    rst = solve(n)
    if rst == False:
        result = 'Case #{}: INSOMNIA\n'.format(case+1)
    else:
        result = 'Case #{}: {}\n'.format(case+1,  rst)
    print n
    print result,


if __name__ == "__main__":
    main()
    #main2()