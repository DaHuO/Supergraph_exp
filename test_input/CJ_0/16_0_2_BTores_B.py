def solve( case ):
    sign = case[0]
    flips = 0
    for c in case:
        if(c != sign):
            if(c == '-'):
                sign = c
                flips = flips + 2
            else:
                sign = c
                
    if(case[0] == '-'):
        flips = flips + 1
    return flips

caseNumbers = input()
for caseN in xrange(1, caseNumbers+1):
    case = raw_input()
    print("Case #%i: %s" % (caseN, solve(case)))
