__author__ = 'cary shindell'

inp = open("lastword.in", 'r')
opt = open("lastword.out", 'w')

N = None
Ss = []

for line in inp:
    if N is None:
        N = int(line)
    else:
        Ss.append(str(line))

results = []

for S in Ss:
    slist = ""
    first = True
    for y in S:
        if y == "\n":
            continue
        if first:
            slist += y
            first = False
            continue
        if y < slist[0]:
            slist += y
        else:
            slist = y + slist
    results.append(slist)

print results

ctr = 1
for x in results:
    opt.write("Case #" + str(ctr) + ": " + x + "\n")
    ctr += 1

inp.close()
opt.close()
