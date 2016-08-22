def solve(s):
    words = list(s)
    rst = []
    last = ""

    for w in words:
        if w >= last:
            last = w
            rst.insert(0, w)
        else:
            rst.append(w)
    return rst

def main():
    #inputFile = "A-small-attempt1.in"
    #inputFile = "A-sample.in"
    inputFile = "A-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        #d, k, n = [int(x) for x in inpf.readline().strip().split(' ')]
        s = inpf.readline().strip()
        rst = solve(s)
        result = 'Case #{}: {}\n'.format(case+1, ''.join(str(v) for v in rst))
        print(result, end="")
        outf.write(result)
    inpf.close()
    outf.close()

def test():
    solve("ABAAB")

if __name__ == "__main__":
    main()
    #test()