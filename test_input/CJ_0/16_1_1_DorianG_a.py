out = open('A/result.txt', 'w')

input = open('A/A-large.in', 'r')
input.readline()
i = 1
for line in input.readlines():
    line = line.strip()
    res = []
    for c in line:
        if len(res) == 0:
            res.insert(0, c)
        elif c >= res[0]:
            res.insert(0, c)
        else:
            res.append(c)
    print("Case #" + str(i) + ": " + "".join(res), file=out)
    i += 1

out.close()
input.close()