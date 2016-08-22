import string

fin = open('cakes.in', 'r')
fout = open('cakes.out', 'w')

n = int(fin.readline())

for x in range(1, n + 1):
    stack = fin.readline()[:-1]
    curr = stack[0]
    print (stack)
    swapc = 0;
    for c in stack:
        if c != curr:
            swapc += 1
            curr = c
    if curr == "-": swapc += 1
    res = "Case #{}: {}\n".format(x, swapc);
    fout.write(res)
    print (res[:len(res) - 1])
