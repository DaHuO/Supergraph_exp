def filterIt(allListItem, stlen, test):
    filtered = []
    for k in range(len(allListItem)-1,-1,-1):
        if len(allListItem[k])==stlen:
            filtered.append(allListItem[k])
        else:
            break

    filtered.sort()
    print 'Case #'+str(test+1)+': '+filtered[(len(filtered)-1)]


t = int(raw_input())

for i in range(t):
    string = raw_input()
    allListItem = []
    startpos = 0
    powervalue = 0
    for j in xrange(len(string)):
        if j==0:
            allListItem.append(string[j])
        else:
            for k in range(startpos,len(allListItem)):
                allListItem.append(string[j]+allListItem[k])
                allListItem.append(allListItem[k]+string[j])

            startpos= startpos+pow(2,powervalue)
            powervalue = powervalue+1
    filterIt(allListItem, len(string), i)
