
def solve(conf):
    conf = reduce(lambda x, y: x if x[-1] == y else x + y, conf, conf[0])
    return len(conf) + ((conf[0] == "+" and len(conf) % 2 == 0) or (conf[0] == "-" and len(conf) % 2 == 1)) - 1

if __name__ == '__main__':
    testcases = int(raw_input())

    for t in xrange(testcases):
        print "Case #{}: {}".format(t + 1, solve(raw_input()))
