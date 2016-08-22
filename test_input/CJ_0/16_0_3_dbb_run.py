import sys

nlines = int(sys.stdin.readline())
casen = 0
while 1:
    line = sys.stdin.readline()
    casen += 1
    if not line:
        break
    length,samples = line.split()
    length = int(length)
    samples = int(samples)
    nfound = 0
    print 'Case #%d:' % casen
    inner = 0
    while nfound < samples:
        inner += 1
        if inner > (2 ** (length -2 ) -1):
            print 'No more solutions'
            break
        n = 2 ** (length - 1) + inner * 2 + 1
        bstr = '{0:b}'.format(n)
        divisors = []
        all_nonprime = True
        for base in range(2, 11):
            basen = int(bstr, base)

            found = False
            i = 2
            while i < int(basen ** 0.5) + 2:
                if basen % i == 0:
                    divisors.append(str(i))
                    found = True
                    break
                i += 1
                # To work with big numbers only try a few
                if i > 100:
                    break
            if not found:
                all_nonprime = False
                break
        if all_nonprime:
            print bstr,
            print ' '.join(divisors)
            nfound += 1
