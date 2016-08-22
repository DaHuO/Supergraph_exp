import sys
data = sys.stdin.readlines()


def solve_str(s):

    last = s[0]
    count = 0

    for i in range(0, len(s)):
        if s[i] != last:
            last = s[i]
            count += 1

    if s[len(s)-1] == "-":
        count += 1

    return count

T = int(data[0])
for i in range(1,T+1):
    string = data[i].rstrip()

    print "Case #"+str(i)+": "+str(solve_str(string))
