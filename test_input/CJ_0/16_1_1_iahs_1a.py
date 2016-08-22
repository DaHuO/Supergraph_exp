import sys
ncases = int(raw_input())
for case in range(ncases):
    s = raw_input()
    out = ""
    for c in s:
        out = out + c if not out or ord(c) < ord(out[0]) else c + out
    print "Case #%d: %s" % (case + 1, out)
