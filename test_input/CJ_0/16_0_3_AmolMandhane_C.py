import math


def get_divisor(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 1

_ = input()
N, J = map(int, raw_input().strip().split(" "))

found = 0
possible = 2**(N - 2)

print "Case #1:"

for mid in xrange(possible):
    midformat = "{0:0%db}" % (N - 2)
    pj = "1" + midformat.format(mid) + "1"
    if possible == 1:
        pj = "11"

    divs = []

    for base in xrange(2, 11):
        div = get_divisor(int(pj, base))
        if div is 1:
            break
        divs.append(div)

    if len(divs) == 9:
        found += 1
        print pj, " ".join(map(str, divs))
        if found == J:
            break
