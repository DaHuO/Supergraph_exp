fp = open("B-large.in",'r')
fw = open("B-large.out", 'w')
t = int(fp.readline().strip())
for case in range(t):
    s = fp.readline().strip() + '+'
    y = sum([not s[i]==s[i+1] for i in range(len(s)-1)])
    fw.write("Case #{0}: {1}\n".format(case+1, y))
fp.close()
fw.close()
