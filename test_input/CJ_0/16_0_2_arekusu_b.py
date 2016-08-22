import sys


def flip(cakes):
    count = 0
    target = "-"
    for i in range(len(cakes)-1, -1, -1):
        if cakes[i] == target:
            count += 1
            target = "+" if target == "-" else "-"
    return count

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    file.readline()
    i = 0
    for line in file:
        i += 1
        if line.strip() == "":
            continue
        r = flip(line)
        print "Case #%d: %s" % (i, r)
