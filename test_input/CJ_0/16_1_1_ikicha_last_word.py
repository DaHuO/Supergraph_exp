def adder(a, b):
    if a == "":
        return b
    else:
        for c in a:
            if c < b:
                return b + a
            elif c > b:
                return a + b
    return a + b


def solve(data):
    return reduce(adder, data)


def main():
    with open("A-input.in") as fin:
        with open("A-output.out", "w") as fout:
            t = int(fin.readline())
            for i in range(0, t):
                data = fin.readline().strip()
                fout.write("Case #%d: %s\n" % (i + 1, solve(data)))


main()
