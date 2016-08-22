import fileinput


n = 0
strings = []
ans = []
for line in fileinput.input():
    if fileinput.isfirstline():
        n = int(line)
    else:
        strings.append(line.strip())
# print(strings)
for line in strings:
    tmp = line[0]
    for i in range(1,len(line)):
        if line[i] < tmp[0]:
            tmp += line[i]
        else:
            tmp = line[i] + tmp
    ans.append(tmp)

f = open('output', 'w')

for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), a))
    f.write('\n')
f.close
