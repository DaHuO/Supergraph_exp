t = raw_input()
t = int(t)
s = ""
x = 1
while x <= t:
    st = raw_input()
    n = len(st)
    k = 0
    while k < n:
        if k==0:
            s = st[k]
        else:
            if st[k] < s[0]:
                s = s + st[k]
            else:
                s = st[k] + s
        k = k + 1
    print "Case #" + str(x) + ": " + s
    x = x + 1
