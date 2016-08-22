fin = open("Pancakes.in", 'r')
fout = open("Pancakes.out", 'w')

n = int(fin.readline())
for i in range(1, n + 1):
    s = fin.readline().strip()
    ans = 0
    if s[0] == '-':
        ans += 1
    p = '-'
    for j in s:
        if p == '+' and j == '-':
            ans += 2
        p = j
    print("Case #{}: {}".format(i, ans))
    fout.write("Case #{}: {}\n".format(i, ans))

fin.close()
fout.close()