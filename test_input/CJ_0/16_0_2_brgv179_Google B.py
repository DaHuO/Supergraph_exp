t = input()
for i in range(t):
    s = raw_input()
    print "Case #"+str(i+1)+": ",
    l = filter(None, s.split('+'))
    count = 2*len(l)
    print count if s[0] == '+' else count - 1