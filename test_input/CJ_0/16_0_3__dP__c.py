n, k = 16, 50
n, k = 32, 500

print ("Case #1:")

1111100000000001
def sol():
    global k
    for i in xrange(0, n - 2, 2):
        for j in xrange(i + 1, n - 2, 2):
            for ii in xrange(j + 1, n - 2, 2):
                for jj in xrange(ii + 1, n - 2, 2):
                    s = ['1'] + ['0'] * (n-2) + ['1']
                    s[i + 1] = '1'
                    s[j + 1] = '1'
                    s[ii + 1] = '1'
                    s[jj + 1] = '1'
                    ss = ''.join(s)
                    for iii in xrange(2, 11):
                        a = int(ss, iii)
                        if (iii % 2 == 0 and a % (iii + 1) != 0) or \
                            (iii % 2 == 1 and a % 2 != 0):
                            continue
                            # print 'BOTVA(%d, %d)' % (i, a % i),
                    print ss, '3 2 5 2 7 2 9 2 11'
                    k -= 1
                    if k == 0:
                        return
sol()
