f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

def flipPancakes(pancakes, i):
    slicePancakes = pancakes[0:i]
    reversedPancakes = reversed(slicePancakes)
    sucReversePancakes = []
    for eachPancake in reversedPancakes:
        if eachPancake == "+":
            sucReversePancakes = ["-"] + sucReversePancakes
        else:
            sucReversePancakes = ["+"] + sucReversePancakes
    return sucReversePancakes + pancakes[i:]


def findTheMostBottomUnHappyPancake(pancakes):
    i = 1
    reversedPancakes = reversed(pancakes)
    for pc in reversedPancakes:
        if pc == "-":
            return len(pancakes) - i + 1
        else:
            i = i + 1
    return None


for t in xrange(T):
    l = f.readline().strip()
    pancakes = [c for c in str(l)]
    numberOfFlip = 0
    while findTheMostBottomUnHappyPancake(pancakes) != None:
        i = findTheMostBottomUnHappyPancake(pancakes)
        pancakes = flipPancakes(pancakes, i)
        numberOfFlip = numberOfFlip + 1
    s = "Case #%d: %d\n" % (t+1, numberOfFlip)
    print s
    o.write(s)