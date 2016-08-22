import sys

sys.stdin.readline()
casen = 0
while 1:
    ln = sys.stdin.readline()
    if not ln:
        break
    casen += 1
    ln = ln.strip()
    out = ''
    for c in ln:
        if len(out) == 0:
            out = c
            continue
        if c < out[0]:
            out += c
        else:
            out = c + out
    print 'Case #%d: %s' % (casen, out)
