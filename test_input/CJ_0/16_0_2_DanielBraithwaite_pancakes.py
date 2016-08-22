def flipEm(s):
    p = s
    flips = 0

    for i in range(1, len(p)):
        if not p[i] == p[i-1]:
            s1 = p[:i]
            s2 = p[i:]
            s3 = flip(s2)
            
            p = flip(p[:i]) + p[i:]
            flips += 1

    if p[0] == '-':
        p = flip(p)
        flips += 1

    print(p)
        
    return flips
    
    

def flip(s):
    r = ""
    for c in s:
        if c == '-':
            r += '+'
        else:
            r += '-'

    return r

o = open('output.txt', 'w+')
f = open('B-large.in', 'r+')
##f = open('test.txt', 'r+')
N = int(f.readline())

for i in range(N):
    s = f.readline().strip()
    
    res = flipEm(s)
    print(res)

    o.write("Case #" + str(i + 1) + ": " + str(res) + "\n")

f.close()
o.close()
