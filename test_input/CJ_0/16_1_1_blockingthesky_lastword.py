def proc(word):
    word = list(word)
    cur = word.pop(0)
    for nxt in word:
        if nxt >= cur[0]:
            cur = nxt + cur
        else:
            cur += nxt
    return cur


inp = open('lastwordlarge.in', 'r')
T = int(inp.readline()) + 1
out = open('lastwordlarge.out', 'w')
for t in xrange(1, T):
    # print "Case #" + str(t) + ":",proc(inp.readline().strip())    
    out.write( "Case #" + str(t) + ": " + proc(inp.readline().strip()) + "\n")

out.close()

