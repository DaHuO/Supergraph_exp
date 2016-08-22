ATTEMPT = 1

#fi = open("B-small-attempt{}.in".format(ATTEMPT), encoding="UTF-8")
fi = open("B-large.in", encoding="UTF-8")
ls = fi.readlines()
T = int(ls[0])
datas = ls[1:]
results = []
assert(T == len(datas))
for data in datas:
    groups = 0
    latest = None
    last = None
    data = data.strip()
    print(repr(data))
    for pancake in data:
        if latest != pancake:
            latest = pancake
            groups += 1
        last = pancake
    print(groups)
    print(last)
    results.append(groups if (last == '-') else (groups - 1))
print(repr(results))

#fo = open("B-small-attempt{}.out".format(ATTEMPT), 'w', encoding="UTF-8")
fo = open("B-large.out", 'w', encoding="UTF-8")
i = 1
for result in results:
    fo.write("Case #{}: ".format(i))
    fo.write(str(result))
    fo.write('\n')
    i += 1
