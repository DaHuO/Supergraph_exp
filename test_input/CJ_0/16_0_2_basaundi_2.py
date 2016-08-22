import sys

def case(S):
    n = 0
    smile = "+"

    for b in S[::-1]:
        if b == smile:
            continue
        n += 1
        if smile == "+":
            smile = "-"
        else:
            smile = "+"
    return n

def main(inps=None):
    if not inps:
        inps = sys.stdin

    lines = iter(inps)
    T = int(next(lines))
    for i in range(T):
        S = next(lines).strip()
        print "Case #%d: %d"%(i + 1, case(S))


if __name__ == "__main__":
    main(sys.stdin)
