import math

t = input()
l, k = map(int, raw_input().strip().split())
print "Case #1:"
counter = 0
n2 = (1 << l - 1)
end = (1 << l) - 1
while n2 < end:
    n2 += 1
    if n2 & 1 == 0:
        continue
    p2, p3, p4, p5, p6, p7, p8, p9, p10 = 1, 1, 1, 1, 1, 1, 1, 1, 1
    n3, n4, n5, n6, n7, n8, n9, n10 = 0, 0, 0, 0, 0, 0, 0, 0
    while p2 < (1 << l):
        if p2 & n2 > 0:
            n3 += p3
            n4 += p4
            n5 += p5
            n6 += p6
            n7 += p7
            n8 += p8
            n9 += p9
            n10 += p10
        p2 *= 2
        p3 *= 3
        p4 *= 4
        p5 *= 5
        p6 *= 6
        p7 *= 7
        p8 *= 8
        p9 *= 9
        p10 *= 10


    def f(n):
        for i in xrange(2, 100):
            if n % i == 0:
                return i
        return 1


    def g(n):
        str = ""
        p = 1
        while n > 0:
            if n % 2 == 1:
                str += '1'
            else:
                str += '0'
            n = n >> 1
        return str[::-1]

    d2, d3, d4, d5, d6, d7, d8, d9, d10 = f(n2), f(n3), f(n4), f(n5), f(n6), f(n7), f(n8), f(n9), f(n10)
    if d2 != 1 and d3 != 1 and d4 != 1 and d5 != 1 and d6 != 1 and d7 != 1 and d8 != 1 and d9 != 1 and d10 != 1:
        counter += 1
        # print (n2, n3, n4, n5, n6, n7, n8, n9, n10)
        print "{} {} {} {} {} {} {} {} {} {}".format(g(n2), d2, d3, d4, d5, d6, d7, d8, d9, d10)
    if counter == k:
        break
print(counter)
