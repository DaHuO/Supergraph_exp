f = open("/Users/aminbarekatain/Desktop/B-large.in")
out = open("/Users/aminbarekatain/Desktop/B-lar.out","w")
def rev(string):
    ret = bytearray("")
    string.reverse()
    for s in string:
        if s == 43:
            ret.append("-")
        else:
            ret.append("+")
    return ret
    
def solve(string):
    if len(string) == 0:
        return 0
    if string[-1] == 43:
        return solve(string[:-1])
    ret = 1
    if string[0] == 43:
        i= string.find("-")
        ret += 1
        string[:i] = rev(string[:i])
    return solve(rev(string)) + ret
    
t = int(f.readline())
for test in xrange(1,t+1):
    out.write("Case #%d: "%test+ str(solve(bytearray(f.readline().strip())))+"\n")
out.close()
