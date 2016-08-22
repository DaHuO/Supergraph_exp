def TheSort(S):
    queue = list()
    for ele in S:
        if len(queue) == 0:
            queue.append(ele)
            continue
        if ord(queue[0]) <= ord(ele):
            queue.insert(0, ele)
        else:
            queue.append(ele)
    return ''.join(queue)
    


f = open("A-large(2).in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().strip()
    print "Case #" + str(x+1) + ": " + str(TheSort(readline))

