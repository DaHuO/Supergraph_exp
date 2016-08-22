f = open('B-large.in')
T = int(f.readline())
f1 = open('B-large.out', 'wc')

for i in range(T):
    input = f.readline().strip()
    current = "+"
    num = 0
    for x in reversed(input):
        if x == current:
            continue
        num += 1
        current = x

    f1.write("Case #%i: " % (i+1))
    f1.write("%i\n" % num)
