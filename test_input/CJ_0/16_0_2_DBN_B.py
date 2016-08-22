
fout = open('b.out', 'w')
fin = open('B-large.in', 'r')

t = int(fin.readline())
for x in range(1,t+1):
    pancakes = fin.readline()
    curr = pancakes[0]
    flipCount = 0
    for p in list(pancakes):
        if p == '\n':
            break
        if curr != p:
            flipCount += 1
        curr = p
    if curr == '-':
        flipCount += 1

    fout.write('Case #{}: {}\n'.format(x, flipCount))
