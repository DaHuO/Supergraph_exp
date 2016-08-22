import ju

results = []
FILE = "A-large"
f = ju.jopen(FILE)

T = int(f.readline())
for t in range(T):
    letters = f.readline()[:-1]
    last = letters[0]
    first = last
    letters = letters[1:]
    for l in letters:
        if l >= first:
            last = l + last
            first = l
        else:
            last = last + l
    print last
    results += [last]


ju.jout(FILE, results)
