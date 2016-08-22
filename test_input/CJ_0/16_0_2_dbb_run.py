import sys

ln = sys.stdin.readline()
casen = 0
while 1:
    line = sys.stdin.readline()
    casen += 1
    if not line:
        break
    line = line.strip()
    pancakes = [c for c in line[::-1]]
    flips = 0
    while '-' in pancakes:
        flip=False
        flips+=1
        for i in range(0, len(pancakes)):
            if pancakes[i] == '-':
                flip = True
            if flip:
                pancakes[i] = '-' if pancakes[i] == '+' else '+'
    print 'Case #%d: %d' % (casen, flips)
