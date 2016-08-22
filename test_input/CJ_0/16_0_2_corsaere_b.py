FILENAME = 'B-large.in'
OUTPUT = 'B-large-response.txt'
with open(FILENAME) as f:
    num_lines = int(f.readline())
    with open(OUTPUT, 'w') as w:
        ctr = 1
        for line in f.readlines():
            flips = 0
            sLine = line.strip()
            for e in range(len(sLine) - 1,-1,-1):
                if line[e] == '+':
                    if flips % 2 != 0:
                        flips += 1
                else:
                    if (flips + 1) % 2 != 0:
                        flips += 1
            w.write("Case #{0}: {1}".format(ctr, flips))
            w.write("\n")
            ctr += 1
