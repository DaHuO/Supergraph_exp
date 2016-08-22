import random

def check_coin(seq):
    checkers = []
    for base in range(2,10+1):
        N = 0
        for i, sym in enumerate(seq):
            # import pdb; pdb.set_trace()
            if sym == '0':
                continue
            ord = len(seq) - i -1
            N += base**ord
        # print 'the number is %s in %s' % (N, base)
        rr = find_divisor(N)
        if not rr:
            return None
        checkers.append(str(rr))
    return "%s %s\n" % (seq, " ".join(checkers))


def find_divisor(N):
    if N==2: return None
    divisor = 3
    bound = min(round(N**0.5) + 8, 100000)
    while divisor < bound:
        if N % divisor == 0:
            return divisor
        divisor += 2
    return None

FILENAME = "large.final.out"
N = 32
J = 500
j = 0



with open(FILENAME, "w") as output:
    output.write("Case #1:\n")
while(j<J):
    # make random string
    coin = "1"
    for _ in range(N-2):
        coin += random.choice(["0","1"])
    coin += "1"
    test = check_coin(coin)
    if not test:
        continue
    j += 1
    with open(FILENAME, "a") as output:
        output.write(test)
    print "found %s of %s: %s " % (j, J, test)
