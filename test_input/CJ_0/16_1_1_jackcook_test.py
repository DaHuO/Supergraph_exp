import sys

fp = file(sys.argv[1])
t = int(fp.next())

of = file('out.txt', 'w+')

for i in range(t):
    s = fp.next().strip()
    ns = s[0]

    for c in range(1, len(s)):
        if ord(ns[0]) <= ord(s[c]):
            ns = s[c] + ns
        else:
            ns += s[c]

    of.write("Case #%d: %s\n" % (i + 1, ns))

of.close()
