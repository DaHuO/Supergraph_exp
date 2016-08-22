def pnext(cur, s):
    return [cur+s, s+cur]

def all_next(big_s):
    states = [big_s[0]]
    for i in range(1, len(big_s)):
        new_states = [ns for s in states for ns in pnext(s, big_s[i])]
        states = new_states

    return states

def last_word(big_s):
    return sorted(all_next(big_s))[-1]


import sys


def parse_file(fname):
    with open(fname, "r") as fh:
        lines = fh.readlines()[1:]

    return [l.strip() for l in lines]

def main():
    fname = sys.argv[1]
    outname = sys.argv[2]

    ns = parse_file(fname)

    answers = [last_word(n) for n in ns]

    with open(outname, "w") as fh:
        for i, a in enumerate(answers, 1):
            fh.write("Case #%i: %s\n" % (i, a))


if __name__ == "__main__":
    main()
