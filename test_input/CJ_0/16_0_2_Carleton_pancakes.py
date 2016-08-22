import sys


def parse_file(fname):
    with open(fname, "r") as fh:
        lines = fh.readlines()[1:]

    return [line.strip() for line in lines]


def collapse(stack):
    if not stack:
        return ""

    cd = [stack[0]]
    for i, p in enumerate(stack[1:]):
        if p == stack[i]:
            continue
        cd.append(p)

    return "".join(cd)


def flip_happy(stack):
    cd = collapse(stack)

    if cd == "+":
        return 0

    if cd == "-":
        return 1

    return 1 + flip_happy(cd[1:])


def main():
    fname = sys.argv[1]
    outname = sys.argv[2]

    ns = parse_file(fname)

    answers = [flip_happy(n) for n in ns]

    with open(outname, "w") as fh:
        for i, a in enumerate(answers, 1):
            fh.write("Case #%i: %s\n" % (i, a))

if __name__ == "__main__":
    main()
