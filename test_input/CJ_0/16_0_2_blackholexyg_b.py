import sys

numCases = int(input())
for kk in range(0,numCases):
    print("Case #%d: " %(kk+1), end="")
    panlist = list(input())

    truelist = []
    truelist.append(panlist[0])

    ii = 0
    while True:
        ii = ii + 1
        if ii>=len(panlist):
            break
        else:
            if panlist[ii]!=panlist[ii-1]:
                truelist.append(panlist[ii])
    if truelist[-1] == "+":
        del truelist[-1]
    print("{}\n".format(len(truelist)), end="")
