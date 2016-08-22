f = open("in", "r")
l = f.readlines()
l = map(lambda x: x[:-1], l)
n = int(l[0])

g = open("out", "w")
def getres(s):
    result = ""
    prevstart = s[0]
    result += prevstart

    for i in range(1, len(s)):
        currletter = s[i]
        if currletter < prevstart:
            result = result + currletter
        else:
            result = currletter + result
            prevstart = currletter

    return result

for i in range(1,n+1):
    result = getres(l[i])
    g.write("Case #" + str(i) + ": " + result + "\n")

f.close()
g.close()
