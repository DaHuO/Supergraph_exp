
T = int(input())

for caseNum in range(1, T+1):
    line = list(input().strip())
    lastPancake = line[-1]
    currentPancake = line[0]
    numFlips = 0
    for pancake in line:
        if pancake != currentPancake:
            currentPancake = pancake
            numFlips += 1
    if lastPancake == '-':
        numFlips += 1

    print("Case #%d: %d" %(caseNum, numFlips))

    
