def pancakeRevenge(pancakes):
    #print pancakes
    
    lastSeenPancake = ""
    # Find first non matching pancake
    for i in range(len(pancakes)):
        if lastSeenPancake == "":
            lastSeenPancake = pancakes[i]
            continue
        else:
            if lastSeenPancake != pancakes[i]:
                break
    # They're all the same
    if i == len(pancakes) - 1 and pancakes[0] == pancakes[-1]:
        if pancakes[0] == "-":
            return 1
        else:
            return 0
    
    else:
        pancakes = swap(pancakes[0:i][::-1]) + pancakes[i:]
        return 1 + pancakeRevenge(pancakes)

        
##    # Find lowest "-" pancake
##    for i in range(len(pancakes)-1,-1, -1):
##        if pancakes[i] == "-":
##            break
##
##    if i == 0 and pancakes[0] == "-":
##        return 1
##    # All pancakes are correctly flipped
##    elif i == 0:
##        return 0
##    else:
##        if pancakes[0] == pancakes[i]:
##            # Flip everything including pancake at i
##            pancakes = swap(pancakes[0:i+1][::-1]) + pancakes[i+1:]
##            return 1 + pancakeRevenge(pancakes)
##        else:
##            # Flip only the ones above the pancake at i
##            pancakes = swap(pancakes[0:i][::-1]) + pancakes[i:]
##            return 1 + pancakeRevenge(pancakes)

def swap(pancakes):
    result = ""
    for pancake in pancakes:
        if pancake == "-":
            result = result + "+"
        else:
            result = result + "-"

    return result

#print pancakeRevenge("+-")
readFile = open("B-large.in")
writeFile = open("B-large.out", "a")

numberOfTestCases = -1
caseNumber = 1
for line in readFile.readlines():
    if(numberOfTestCases == -1):
        numberOfTestCases = int(line)
        continue

    writeFile.write("Case #" + str(caseNumber) + ": " + str(pancakeRevenge(line.strip())) + "\n")
    caseNumber = caseNumber + 1

readFile.close()
writeFile.close()
