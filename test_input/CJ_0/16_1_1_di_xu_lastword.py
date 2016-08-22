import sys
f = sys.stdin
fout = open("/Users/dixu/Desktop/Algorithms/googleCodeJam/2016Round1A/result.txt","w")
cases = int(f.readline())
for case in range(1,cases+1):
    word = f.readline()
    res = ""
    for i in word:
        if not res:
            res += i
        elif i < res[0]:
            res = res+i
        else:
            res = i+res
    fout.write("Case #%d: %s" % (case,res))
