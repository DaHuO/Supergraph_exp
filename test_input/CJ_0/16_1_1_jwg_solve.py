#google code jam I/O template


def solve(chars):
    if len(chars) <= 1:
        return chars
    latestChar = max(chars)
    index = chars.find(latestChar)
    return latestChar * chars.count(latestChar) + solve(chars[:index]) + chars[index+1:].replace(latestChar, "")



numCases = input()
for caseNum in range(1, numCases+1):
    #read single-line input
    chars = raw_input()
    ans = solve(chars)
    print "Case #%d: %s" % (caseNum, str(ans))







