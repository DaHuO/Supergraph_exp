n_t = int(raw_input().strip())
for t in xrange(1, n_t+1):
    l = raw_input().strip()
    final_str = ""
    for c in l:
        if final_str == "":
            final_str = c
        elif ord(final_str[0]) <= ord(c):
            final_str = c + final_str
        else:
            final_str = final_str + c
    print "Case #{0}: {1}".format(t, final_str)

