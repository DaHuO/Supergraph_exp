import sys

    
T = int(sys.stdin.readline())
case = 1
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0:
        ret = ""
        for c in s:
            if len(ret) == 0 or c >= ret[0]:
                ret = c + ret
            else:
                ret = ret + c
        print "Case #{0}:".format(case), ret
    case += 1
        
