

fin = open('words.in', 'r')
fout = open('cakes.out', 'w')

t = int(fin.readline())

for x in range(1, t + 1):
    s = fin.readline()[:-1] # without \n
    res = s[0]
    cr = cl = res[0]
    for c in range(1, len(s)):
        if (cl > s[c]):
            res += s[c]
            cr = s[c]
        else:
            res = s[c] + res
            cl = s[c]
    res = "Case #{}: {}\n".format(x, ''.join(res))
    fout.write(res)
    print(res)